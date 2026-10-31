# Economic Theory for AI Alignment — PhD thesis

University of Warwick, Department of Computer Science. Author: Abhimanyu Pallavi Sudhir.

## Building

```bash
latexmk -pdf main.tex     # produces main.pdf (settings in ./latexmkrc)
```

After editing any `bib/<chapter>.bib`, regenerate the merged bibliography:

```bash
python3 tools/merge_bibs.py   # writes bib/thesis.bib (deduped by key, first wins)
```

## Structure

| Chapter file | Source | 
|---|---|
| `chapters/intro.tex` | y2 report intro, `alignment_summary.org`, `ways_to_think_alignment.org`, marketic-agents intro |
| Part I: Economic theory of agency | |
| `chapters/market-rl.tex` | "Market-based architectures in RL and beyond" (y2 report, `chaps/mba.tex`) |
| `chapters/agency.tex` | marketgrad-theory articles ("Price recursion…", "Bregman divergences…"; incl. the alignment lemma from the research notes) + marketgrad library |
| Part II: Information asymmetry and scalable oversight | |
| `chapters/infonomy.tex` | "Extrapolating Volition with Recursive Information Markets" (infonomy-paper) |
| `chapters/solib.tex` | "A Benchmark for Scalable Oversight Mechanisms" (solib-paper) |
| Part III: Eliciting beliefs on subjective questions | |
| `chapters/nonvf.tex` | MERGE: succinct AAMAS version (narrative backbone) + long arXiv version (program-market construction, full results, Garrabrant appendix) |
| `chapters/consistency.tex` | "Consistency Checks for Language Model Forecasters" (ICLR 2025), restructured: checks table + arbitrage/frequentist metric theory promoted from appendix into the main narrative |
| `chapters/arbitrage.tex` | New (unpublished), all draft-marked: marketgrad-theory "Markets are arbitrageurs" + lvpm `notes/latent-meaning.md` (numbers reproduced by those repos' scripts) |

`chapters/part{1,2,3}-intro.tex` are part-opening texts (no chapter heading). Each part then has a literature review, `chapters/litrev-{agency,oversight,subjective}.tex`, merged from the papers' related-work sections; `litrev/<paper>.tex` keeps verbatim copies of those sections for reference (not compiled).

Each chapter opens with a draft-marked "bridge" introduction, followed by the paper's own introduction trimmed to its contributions (passages duplicated by the thesis or part introductions are commented out, marked `[dup of ...]`), and ends its introduction with a `notation` table (`\notn{symbol}{meaning}`, defined in `preamble/thesis.tex`).

## Conventions

See `CONVENTIONS.md`. Key points:

- **All newly composed "glue" text is marked** with `\draft{...}` or `\begin{draftblock}...\end{draftblock}` — it renders dark red with a `[draft]` margin tag. Set `\draftfinaltrue` in `preamble/thesis.tex` to typeset it as normal text for submission.
- Text lifted from the papers/reports is *not* marked.
- Research questions and contributions in the introduction use the `researchquestion` / `contribution` environments (preamble/thesis.tex): RQs are numbered RQ1, RQ2, …; a `contribution` box takes the number of the preceding RQ. Label RQs with `\label{rq:...}` and refer with `\cref`.
- Citations: always `\citep` (parenthetical) or `\citet` (textual); never bare `\cite`. New references that were previously `\href` links live in `bib/intro.bib`.
- Chapter-local macros live in `macros/<chapter>.tex`, loaded inside a group by `\thesischapter` so chapters can override shared macros (e.g. `\bools`, `\Prob`). They are also pre-loaded (tolerantly, last-wins) for the ToC/LoF/LoT pass — so any macro used in a caption or section heading must live in the macros file, not inline in the chapter, and the macro files must be safe to load twice (guard `\newcounter` etc.).

## Humanizing AI-written text (StealthGPT)

AI-written text is exactly the draft-marked text. `tools/humanize.py` rewrites it with StealthGPT, paragraph by paragraph, sending LaTeX only as opaque placeholders (`[[X3]]`) because StealthGPT edits text inside its own "preserved" spans. Every rewrite was then checked against its original for meaning; `tools/humanize/units.json` records original, StealthGPT output and the meaning-corrected `final` for each unit, and `tools/humanize/review.md` shows them side by side.

```
python3 tools/humanize.py extract      # collect draft paragraphs (>= 25 prose words) not yet done
python3 tools/humanize.py send         # StealthGPT (STEALTHGPT_API_KEY)
python3 tools/humanize.py review       # side-by-side review.md; correct "final" in units.json
python3 tools/humanize.py apply        # write finals into the .tex files
python3 tools/humanize.py pangram      # AI-detection check (PANGRAM_API_KEY)
```

New or edited draft text must go through the same loop: `extract` keeps results for unchanged paragraphs.

## Known TODOs (grep for `%% TODO` and `\draft`)

- Acknowledgements are a placeholder; titlepage date is draft-marked.
- `\infonomyurl` still points to the anonymized review URL.
- Part III intro's characterization of Conitzer (2012)'s two-layer construction should be verified against the paper.
- The agency chapter keeps the source articles' literal equation-tag numbering ; harmonize before submission.
- Pangram AI-detection check not yet run: the Pangram account had no credits ("Insufficient credits"). Run `python3 tools/humanize.py pangram` once topped up.
