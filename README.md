# Economic Theory for AI Alignment

This repository is the working LaTeX source for Abhimanyu Pallavi Sudhir's
University of Warwick PhD thesis. The current draft is a standalone compilation
of manuscript material from the surrounding research repositories, arranged as
three parts:

1. economic theory of agency;
2. information asymmetry and scalable oversight; and
3. eliciting beliefs on subjective questions.

See [SOURCE_MAP.md](SOURCE_MAP.md) for the origin and adaptation status of each
chapter.

## Build

The build requires `latexmk`, BibTeX, and a reasonably complete TeX Live
installation (including `tcolorbox`, `pgfplots`, `algorithmicx`, `todonotes`,
and `pythonhighlight`). Run:

```sh
make thesis
```

The resulting thesis is `main.pdf`. `make clean` removes intermediate files;
`make distclean` also removes the PDF.

## Draft glue

Text newly written to connect the imported papers is deliberately explicit in
the source and the PDF:

```tex
\begin{drafttext}
Text requiring author review.
\end{drafttext}
```

This renders as a yellow box headed **DRAFT GLUE — AUTHOR REVIEW REQUIRED**.
The boxes should be revised by the author and converted to ordinary prose only
when their claims and voice have been approved. `\chapterprovenance{...}` marks
source notes for imported material.

## Editing policy

The paper text is copied into this repository so that the thesis remains
buildable without sibling checkouts. Edits made in a paper repository are not
automatically synchronized: use the source map when refreshing a chapter and
review the resulting diff, rather than overwriting a thesis chapter blindly.
