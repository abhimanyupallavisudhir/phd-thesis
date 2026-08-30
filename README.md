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

`chapters/part{1,2,3}-intro.tex` are part-opening texts (no chapter heading).

## Conventions

See `CONVENTIONS.md`. Key points:

- **All newly composed "glue" text is marked** with `\draft{...}` or `\begin{draftblock}...\end{draftblock}` — it renders dark red with a `[draft]` margin tag. Set `\draftfinaltrue` in `preamble/thesis.tex` to typeset it as normal text for submission.
- Text lifted from the papers/reports is *not* marked.
- Chapter-local macros live in `macros/<chapter>.tex`, loaded inside a group by `\thesischapter` so chapters can override shared macros (e.g. `\bools`, `\Prob`). They are also pre-loaded (tolerantly, last-wins) for the ToC/LoF/LoT pass — so any macro used in a caption or section heading must live in the macros file, not inline in the chapter, and the macro files must be safe to load twice (guard `\newcounter` etc.).

## Known TODOs (grep for `%% TODO` and `\draft`)

- Acknowledgements are a placeholder; titlepage date is draft-marked.
- `\infonomyurl` still points to the anonymized review URL.
- Part III intro's characterization of Conitzer (2012)'s two-layer construction should be verified against the paper.
- The agency chapter keeps the source articles' literal equation-tag numbering ; harmonize before submission.
