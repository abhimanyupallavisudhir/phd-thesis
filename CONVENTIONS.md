# Thesis compilation conventions

Thesis root: `/home/user/karmax/phd-thesis/`. Built with `latexmk -pdf main.tex` (pdflatex + bibtex/natbib).

## Structure

- `main.tex` — document skeleton; loads each chapter via `\thesischapter{<name>}`.
- `chapters/<name>.tex` — chapter body. Starts with `\chapter{...}\label{ch:<name>}`, then uses `\section`, `\subsection`, ... (a paper's `\section` becomes a thesis `\section`; do NOT renumber into chapters).
- `macros/<name>.tex` — chapter-local macros. Loaded *inside a group*, so redefinitions of common macros are safe here and vanish after the chapter. Use `\DeclareDocumentCommand`/`\RenewDocumentCommand` when overriding an existing command (e.g. `\bools`), `\NewDocumentCommand`/`\newcommand` for fresh ones. **Never** `\usepackage` here (preamble-only); if a package is missing, note it at the top of the chapter file in a `%% TODO` comment.
- `figs/<name>/` — figure assets for the chapter, copied from the source repo. Reference as `figs/<name>/file.ext`.
- `bib/<name>.bib` — verbatim copy of the source paper's `.bib` file(s) (they get merged into `bib/thesis.bib` later; don't do the merge yourself).

## Already defined globally (do not redefine in chapter macro files unless the chapter needs a *different* meaning)

- Packages: amsmath/amssymb/amsfonts/amsthm, mathtools, mathrsfs, nicefrac, xfrac, graphicx, caption, subcaption, booktabs, longtable, tabularx, threeparttable, wrapfig, float, tikz (calc), pgfplots, algorithm, algpseudocode (noend), pythonhighlight, enumitem, changepage, mdframed, pifont (`\xmark`), tcolorbox, verbatim, natbib, appendix, hyperref, cleveref, todonotes (disabled).
- Theorem envs (numbered within chapter): `theorem, nontheorem, proposition, lemma, corollary, definition, lefinition, example, assumption, remark`; unnumbered: `remark*, notation*, setup*, notes*, constants*`; also `hproof` (proof sketch) and `thesisclaim` (centred bold-italic display; renamed from the papers' `thesis` env — rename usages).
- Macros: `\Nats \Rats \Ints \Reals \bools \Bools \probs \none \boolsopt \zero \Powerset \Props \strings \finset \supp \Indicator \eps \abs \norm \argmax \argmin \Prob \Probof \Expect \Expectof \Expectofu \sigalg \sigalgalt \Sigalg \textsigalg \textsubsigalg \nicett \xmark \cmark`.
- Todo commands (`\manyu`, `\towrite`, `\rephrase`, `\dpaleka`, ...) and box envs (`promptbox`, `emptypromptbox`, `questionbox`) and pastel colours.
- `\bools` is globally `\{\top,\bot\}`; `\Prob` is globally `\mathbf{P}` — override per chapter if the source paper differs.

## Content rules

1. **Lift text verbatim from the source papers wherever possible.** This is a compilation, not a rewrite.
2. Any *newly composed* glue/transition text must be wrapped in `\draft{...}` (inline) or `\begin{draftblock}...\end{draftblock}` (paragraphs). Do not silently author new prose.
3. Drop conference boilerplate: `\maketitle`, author blocks, CCS concepts, copyright, acknowledgements, reproducibility/ethics statements, page-limit hacks (`\vspace` tweaks, `\balance`).
4. The paper's abstract becomes the chapter opener via `\chapterabstract{...}` placed right after `\chapter{...}\label{...}`; precede it (or follow it) with a `\chaptersource{...}` note stating which paper the chapter is based on (with coauthors/venue).
5. Paper appendices that should stay appendices go at the end of the chapter inside `\begin{subappendices} ... \end{subappendices}` (sections inside become e.g. "5.A").
6. Keep `\citep`/`\citet`/`\cite` as-is (natbib, author-year plainnat).
7. Labels: prefix all labels with the chapter name to avoid collisions, e.g. `\label{infonomy:sec:bayesian}`, and fix internal `\ref`/`\cref` accordingly.
8. Use `subcaption` (`subfigure`/`subtable` environments), never the old `subfigure` package's `\subfigure` command — convert if the source uses it.
9. LaTeX must compile under pdflatex. If something can't compile without a missing asset, comment it out with a `%% TODO(<name>): ...` note rather than deleting.
