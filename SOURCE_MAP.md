# Thesis source map

This map records where the first thesis compilation came from. Paths are
relative to the shared `/home/user/karmax` workspace. “Imported” means paper
prose was copied or mechanically converted and then minimally adapted for the
book-level LaTeX build. “Draft glue” means newly composed text visibly marked
with the `drafttext` environment.

| Thesis material | Primary source | Status |
| --- | --- | --- |
| Introduction | `notyet_research/reports/phd/y2_annual_report/main.tex` and the introductions of the manuscripts listed below | Draft glue, informed by source prose |
| Part I introduction: Markets as Agents | `notyet_research/reports/phd/y2_annual_report/mba.tex`, `rim.tex`, and `marketgrad-theory/Price recursion is the rational theory of reward.md` | Draft glue |
| Market-Based Architectures in Reinforcement Learning and Beyond | `notyet_research/reports/phd/y2_annual_report/chaps/mba.tex` and `chaps/pre_mba.tex` | Imported thesis-ready paper text |
| Price Recursion as a Rational Theory of Reward | `marketgrad-theory/Price recursion is the rational theory of reward.md` | Imported via Pandoc; heading numbering normalized |
| Reward Is Hyperstitional Information (precedent within the price-recursion chapter) | `marketgrad-theory/Bregman divergences, mirror ascent and reward as hyperstitious information.md` | Imported via Pandoc |
| `marketgrad` implementation note | `marketgrad/README.md` | Imported short implementation context; the code-level `marketgrad/SPEC.md` is not reproduced |
| Part II introduction: Information Asymmetry as an Alignment Problem | Introductions of `infonomy-paper/main.tex` and `solib-paper/main.tex` | Draft glue |
| Extrapolating Volition with Recursive Information Markets | `infonomy-paper/main.tex` | Imported from the current manuscript, including main-text algorithms and figures |
| A Benchmark for Scalable Oversight Mechanisms | `solib-paper/main.tex` | Imported from the current manuscript, including main-text figures and results table |
| Part III introduction: Markets without Immediate Ground Truth | `notyet_research/reports/phd/y2_annual_report/vf.tex`, `cfc.tex`, and the corresponding paper introductions | Draft glue |
| Betting on What Is Neither Verifiable nor Falsifiable | `notyet_research/reports/phd/y2_annual_report/chaps/vf.tex` | Imported thesis-ready paper text |
| Consistency Checks for Language Model Forecasters | `notyet_research/reports/phd/y2_annual_report/chaps/cfc.tex` plus `chaps/app/*.tex` | Imported thesis-ready paper text and appendices |
| Bibliography | `notyet_research/reports/phd/y2_annual_report/refs.bib`, `notyet_research/reports/phd/y2_annual_report/refscfd.bib`, `infonomy-paper/refs.bib`, `solib-paper/refs.bib`, and `solib-paper/refs_custom.bib` | Merged and deduplicated with `bibtool` |

Figures used by the imported chapters are copied under `figures/` so the build
is self-contained. The older recursive-market algorithm source from the annual
report is staged under `appendices/`, but the current manuscript's main-text
algorithms are the ones included in the compiled thesis.

## Material still needed or awaiting an editorial decision

- The official Warwick thesis template or current formatting checklist was not
  present. The current `book` layout is a conservative A4 working format, not a
  claim of final regulatory compliance.
- The final Warwick declaration wording, supervisor details, submission date,
  and acknowledgements were not present. Their placeholders are marked as draft.
- The Part III introduction names Conitzer's cooperative-game account and the
  two-layer mechanism as an editorial direction, but no local copy of that
  primary manuscript was provided. A fuller treatment should be added once the
  intended edition/source is supplied.
- If a newer standalone TeX source exists for the market-based RL paper, it
  should replace the annual-report snapshot after a controlled comparison.
- The first compilation prioritizes each paper's main argument. Large
  implementation/protocol appendices from `infonomy-paper` and `solib-paper`
  are not yet incorporated; they can be selected later instead of copying all
  supplementary material indiscriminately.
- Imported manuscripts retain some author `\todo{...}` annotations and several
  wide paper-format equations/tables. These are valuable revision markers for
  now, but must be resolved or re-typeset before submission.
