LATEXMK ?= latexmk
THESIS_SOURCES := $(shell find chapters frontmatter appendices figures -type f) \
	main.tex preamble.tex references.bib

.PHONY: all thesis clean distclean

all: thesis

thesis: main.pdf

main.pdf: $(THESIS_SOURCES)
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex

clean:
	$(LATEXMK) -c main.tex

distclean:
	$(LATEXMK) -C main.tex
