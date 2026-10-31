#!/usr/bin/env python3
"""Humanize AI-written (draft-marked) prose in the thesis with StealthGPT.

The supervisor asked that all AI-written text be passed through StealthGPT so
that its tone reads naturally. In this repository AI-written text is exactly
the text inside \\draft{...} and \\begin{draftblock}...\\end{draftblock}, so this
tool works on those regions only, and only on prose:

  * a unit is one paragraph (blank-line separated) inside a draft region;
  * units containing environments (\\begin/\\end), display maths, comment lines
    or fewer than MIN_WORDS words of prose are skipped (short connective
    phrases, theorem statements, proofs, lists, tables);
  * every LaTeX construct (maths, commands with their arguments, ties, quotes
    of the form ``...'') is frozen with StealthGPT's [[...]] preservation
    markers, and the reply is rejected unless every frozen span comes back
    verbatim and exactly once.

Workflow (state is kept in tools/humanize/, which is committed so that every
rewrite can be audited against its original):

  python3 tools/humanize.py extract            # -> tools/humanize/units.json
  python3 tools/humanize.py send [--model M]   # StealthGPT; -> units.json
  python3 tools/humanize.py review             # -> tools/humanize/review.md
  #   ... check each rewrite means what the original meant; edit the
  #   "final" field in units.json where it does not ...
  python3 tools/humanize.py apply              # write "final" texts into .tex
  python3 tools/humanize.py pangram            # optional AI-detection check

Environment: STEALTHGPT_API_KEY, PANGRAM_API_KEY.
"""
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "tools" / "humanize"
UNITS = STATE / "units.json"
FILES = sorted((ROOT / "chapters").glob("*.tex")) + sorted((ROOT / "frontmatter").glob("*.tex"))
MIN_WORDS = 25
BATCH_WORDS = int(os.environ.get("HUMANIZE_BATCH_WORDS", "1200"))
SEP = "[[@@U{}@@]]"


# ----------------------------------------------------------------- regions
def match_brace(s, i):
    """s[i] == '{'; return index just past the matching '}'."""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    raise ValueError("unbalanced braces")


def draft_regions(s):
    """Yield (start, end) of the *contents* of draft regions in s."""
    for m in re.finditer(r"\\begin\{draftblock\}", s):
        e = s.index(r"\end{draftblock}", m.end())
        yield m.end(), e
    for m in re.finditer(r"\\draft\{", s):
        # skip commented-out occurrences
        line_start = s.rfind("\n", 0, m.start()) + 1
        if "%" in s[line_start:m.start()].replace("\\%", ""):
            continue
        b = m.end() - 1
        e = match_brace(s, b)
        yield b + 1, e - 1


# ------------------------------------------------------------- protection
FROZEN_ENVS = r"(?:equation|align|gather|multline|table|figure|tabular|tikzpicture|longtable)\*?"
PROTECT_RE = re.compile(
    r"""(
      \\begin\{(?P<env>""" + FROZEN_ENVS + r""")\}.*?\\end\{(?P=env)\}   # whole display/table envs
    | %[^\n]*(?:\n|$)                             # comment lines
    | \$\$.*?\$\$ | \$(?:\\.|[^$\\])+\$          # inline / display maths
    | \\\[.*?\\\] | \\\(.*?\\\)
    | ``|''                                       # TeX quotes
    | ~                                           # ties
    | \\[A-Za-z@]+\*?(?:\s*\[[^\]]*\])*(?:\s*\{)?  # a command (+ opt args, + '{' handled below)
    | \\[^A-Za-z]                                 # \%, \&, \\, \, ...
    )""",
    re.X | re.S,
)


def protect(text):
    """Return (prompt, spans): text with each LaTeX span replaced by an opaque
    placeholder [[Xn]]. StealthGPT rewrites text *inside* literal [[...]]
    markers (spacing in maths, \\cref -> \\Cref, invented labels), so the
    LaTeX itself is never sent."""
    out, spans, i = [], [], 0
    while i < len(text):
        m = PROTECT_RE.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i:m.start()])
        tok = m.group(0)
        end = m.end()
        if tok.startswith("\\") and tok.rstrip().endswith("{") and not m.group("env"):
            end = match_brace(text, m.end() - 1)
            while end < len(text) and text[end] == "{":
                end = match_brace(text, end)
            if tok.startswith("\\begin"):
                mm = re.match(r"\s*\[[^\]]*\]", text[end:])
                if mm:
                    end += mm.end()
                mm = re.match(r"\s*\\label\{[^}]*\}", text[end:])
                if mm:
                    end += mm.end()
            tok = text[m.start():end]
        if tok == "~":            # a tie is just a space to the rewriter
            out.append(" ")
            i = end
            continue
        if tok in ("``", "''"):   # TeX quotes become plain quotes; tidy() restores them
            out.append('"')
            i = end
            continue
        out.append(f"[[X{len(spans)}]]")
        spans.append(tok)
        i = end
    return "".join(out), spans


def unprotect(reply, spans):
    """Restore placeholders; every one must come back exactly once."""
    text = re.sub(r"\[+\s*(X\d+)\s*\]+", r"[[\1]]", reply)
    found = re.findall(r"\[\[X(\d+)\]\]", text)
    want = [str(k) for k in range(len(spans))]
    if sorted(found, key=int) != want:
        return None, {"missing": sorted(set(want) - set(found), key=int),
                      "duplicated_or_extra": [f for f in found if found.count(f) > 1 or f not in want]}
    text = tidy(text)  # tidy the prose before re-inserting LaTeX
    text = re.sub(r"\[\[X(\d+)\]\]", lambda m: "\x00" + m.group(1) + "\x00", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], text)
    # restore ties before references (they were sent as plain spaces)
    text = re.sub(r"(?<=\w) (\\(?:ref|eqref|pageref)\{)", r"~\1", text)
    return fix_cref_case(text), None


def fix_cref_case(t):
    """\\Cref at the start of a sentence, \\cref elsewhere (placeholders move)."""
    def rep(m):
        before = t[:m.start()].rstrip()
        abbrev = re.search(r"(?:\be\.g|\bi\.e|\bcf|\bvs|\betc)\.$", before)
        start = (not before) or (before[-1] in ".!?" and not abbrev) or before.endswith("\\par")
        return ("\\Cref" if start else "\\cref") + m.group(1)
    return re.sub(r"\\[cC]ref(\{)", rep, t)


def tidy(t):
    t = t.replace("\u201c", "``").replace("\u201d", "''").replace("\u2019", "'").replace("\u2018", "`")
    t = t.replace("\u2014", "---").replace("\u2013", "--").replace("\u00a0", " ")
    t = re.sub(r'"([^"]+)"', r"``\1''", t)
    t = re.sub(r"(?<!\\)%", r"\\%", t)
    t = re.sub(r"(?<!\\)&", r"\\&", t)
    t = re.sub(r"[ \t]+", " ", t).strip()
    return t


def prose_words(text):
    p, _ = protect(text)
    return len(re.sub(r"\[\[.*?\]\]", " ", p, flags=re.S).split())


def paragraphs(region):
    """Blank-line paragraphs, merged so that no environment is split."""
    out, cur, depth = [], [], 0
    for para in re.split(r"\n\s*\n", region):
        body = re.sub(r"%[^\n]*", "", para)
        depth += len(re.findall(r"\\begin\{", body)) - len(re.findall(r"\\end\{", body))
        cur.append(para)
        if depth <= 0:
            core = "\n\n".join(cur).strip()
            if core:
                out.append(core)
            cur, depth = [], 0
    if cur and "\n\n".join(cur).strip():
        out.append("\n\n".join(cur).strip())
    return out


# --------------------------------------------------------------- commands
def extract():
    units = []
    for f in FILES:
        s = f.read_text()
        for a, b in draft_regions(s):
            region = s[a:b]
            for core in paragraphs(region):
                if prose_words(core) < MIN_WORDS:
                    continue
                units.append({"id": len(units), "file": str(f.relative_to(ROOT)), "original": core})
    STATE.mkdir(parents=True, exist_ok=True)
    old = {}
    if UNITS.exists():
        old = {(u["file"], u["original"]): u for u in json.loads(UNITS.read_text())}
    for u in units:  # keep earlier results for unchanged units
        prev = old.get((u["file"], u["original"]))
        if prev:
            u.update({k: v for k, v in prev.items() if k not in ("id",)})
    UNITS.write_text(json.dumps(units, indent=1, ensure_ascii=False))
    total = sum(prose_words(u["original"]) for u in units)
    print(f"{len(units)} units, {total} prose words -> {UNITS}")


def stealth(prompt, model):
    body = {"prompt": prompt, "rephrase": True, "model": model, "preservation": True}
    req = urllib.request.Request(
        "https://www.stealthgpt.ai/api/stealthify",
        data=json.dumps(body).encode(),
        headers={"api-token": os.environ["STEALTHGPT_API_KEY"], "Content-Type": "application/json"},
    )
    for attempt in range(3):
        try:
            return json.load(urllib.request.urlopen(req, timeout=600))
        except Exception as e:  # noqa: BLE001
            print("  retry:", e)
            time.sleep(5)
    raise RuntimeError("StealthGPT failed")


def send(model="super"):
    units = json.loads(UNITS.read_text())
    todo = [u for u in units if not u.get("humanized")]
    # batch consecutive units from the same file
    batches, cur, words = [], [], 0
    for u in todo:
        w = prose_words(u["original"])
        if cur and (cur[-1]["file"] != u["file"] or words + w > BATCH_WORDS):
            batches.append(cur)
            cur, words = [], 0
        cur.append(u)
        words += w
    if cur:
        batches.append(cur)
    for bi, batch in enumerate(batches):
        parts, spans = [], []
        for k, u in enumerate(batch):
            p, sp = protect(u["original"])
            u["_spans"] = sp
            parts.append((SEP.format(k) + " " if k else "") + p)
        prompt = " ".join(parts)
        r = stealth(prompt, model)
        res = r["result"]
        print(f"batch {bi+1}/{len(batches)}: {len(batch)} units, score {r.get('howLikelyToBeDetected')}, "
              f"spent {r.get('wordsSpent')}, left {r.get('remainingCredits')}")
        pieces = re.split(r"\[\[+@@U(\d+)@@\]\]+", res)
        texts = {0: pieces[0]}
        for j in range(1, len(pieces) - 1, 2):
            texts[int(pieces[j])] = pieces[j + 1]
        for k, u in enumerate(batch):
            if k not in texts:
                u["error"] = "separator lost"
                continue
            out, err = unprotect(texts[k], u.pop("_spans"))
            if err:
                u["error"] = err
                u["raw"] = texts[k]
            else:
                u.pop("error", None)
                u["humanized"] = out
                u["model"] = model
                u["detector_score"] = r.get("howLikelyToBeDetected")
        UNITS.write_text(json.dumps(units, indent=1, ensure_ascii=False))
    bad = [u["id"] for u in units if u.get("error")]
    print("units with errors:", bad)


def review():
    units = json.loads(UNITS.read_text())
    out = ["# Humanization review\n", "Each unit: original (AI-written draft) vs humanized (StealthGPT) vs final.\n"]
    for u in units:
        out.append(f"\n## Unit {u['id']} — {u['file']}\n")
        out.append("**Original**\n\n" + u["original"] + "\n")
        out.append("**Humanized**\n\n" + u.get("humanized", "(none)") + "\n")
        if u.get("final") and u["final"] != u.get("humanized"):
            out.append("**Final (meaning-corrected)**\n\n" + u["final"] + "\n")
        if u.get("note"):
            out.append("*Note:* " + u["note"] + "\n")
    (STATE / "review.md").write_text("\n".join(out))
    print("wrote", STATE / "review.md")


def apply():
    units = json.loads(UNITS.read_text())
    by_file = {}
    for u in units:
        new = u.get("final") or u.get("humanized")
        if new and new != u["original"]:
            by_file.setdefault(u["file"], []).append((u["original"], new))
    for fn, reps in by_file.items():
        p = ROOT / fn
        s = p.read_text()
        for old, new in reps:
            n = s.count(old)
            if n != 1:
                print(f"  ! {fn}: original found {n} times, skipped: {old[:60]}...")
                continue
            s = s.replace(old, new)
        p.write_text(s)
        print(f"{fn}: {len(reps)} units applied")


def pangram():
    units = json.loads(UNITS.read_text())
    key = os.environ["PANGRAM_API_KEY"]
    text = "\n\n".join(re.sub(r"\[\[(.*?)\]\]", " ", protect(u.get("final") or u.get("humanized") or u["original"])[0])
                       for u in units)
    req = urllib.request.Request("https://text.external-api.pangram.com/task",
                                 data=json.dumps({"text": text}).encode(),
                                 headers={"x-api-key": key, "Content-Type": "application/json"})
    tid = json.load(urllib.request.urlopen(req, timeout=120))
    print(tid)
    if "task_id" not in tid:
        return
    while True:
        time.sleep(5)
        r = json.load(urllib.request.urlopen(urllib.request.Request(
            f"https://text.external-api.pangram.com/task/{tid['task_id']}", headers={"x-api-key": key}), timeout=120))
        if r.get("stage") in ("STAGE_SUCCESS", "STAGE_FAILED"):
            (STATE / "pangram.json").write_text(json.dumps(r, indent=1))
            print({k: r.get(k) for k in ("stage", "fraction_ai", "fraction_ai_assisted", "fraction_human", "headline")})
            return


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "extract"
    if cmd == "send":
        model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "super"
        send(model)
    else:
        {"extract": extract, "review": review, "apply": apply, "pangram": pangram}[cmd]()
