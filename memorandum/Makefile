### Makefile for LaTeX
### 
### Carlos Garcia Campos <carlosgc@gnome.org>
###

LATEX=latex
DVIPS=dvips
PS2PDF=ps2pdf
BIBTEX=bibtex
MKINDEX=makeindex
CHECK=lacheck
SPELL=aspell
LATEX2HTML=latex2html

NAME=memorandum

DVI=$(NAME).dvi
PS=$(NAME).ps
PDF=$(NAME).pdf
TEX=$(NAME).tex
IDX=$(NAME).idx
LOG=$(NAME).log
PS2PDF_ARGS=-dPDFSETTINGS=/printer -dCompatibilityLevel=1.4 -dMaxSubsetPct=100 -dSubsetFonts=true -dEmbedAllFonts=true -sPAPERSIZE=a4
DVIPS_ARGS=-t a4 -Ppdf

all: $(DVI)

RERUN = '(There were undefined references|Rerun to get (cross-references|the bars) right)'
RERUNBIB = 'No file.*\.bbl|Citation.*undefined'
UNDEFINED = '((Reference|Citation).*undefined)|(Label.*multiply defined)'

$(DVI): $(TEX)
	@echo "====> LaTeX first pass"
	@$(LATEX) $<
	@if egrep -q $(RERUNBIB) $(LOG) ; then echo "====> BibTex" && $(BIBTEX) $(NAME) && echo "====> LaTeX BibTeX pass" && $(LATEX) $< ; fi
	@if egrep -q $(RERUN) $(LOG) ; then echo "====> LaTeX rerun" && $(LATEX) $<; fi
	@if egrep -q $(RERUN) $(LOG) ; then echo "====> LaTeX rerun" && $(LATEX) $<; fi
	@echo "====> Undefined references and citations:"
	@egrep -i $(UNDEFINED) $(LOG) || echo "None."
	@echo "====> Dimensions:"
	@grep "dimension:" $(LOG) || echo "None."

$(PS): $(DVI)
	@echo "====> Generating PostScript"
	$(DVIPS) $(DVIPS_ARGS) $(DVI)

$(PDF): $(PS)
	@echo "====> Generating PDF"
	$(PS2PDF) $(PS2PDF_ARGS) $(PS)

ps: $(PS)

pdf: $(PDF)

html1: $(TEX)
	@echo "====> Generating HTML (One file)"
	$(LATEX2HTML) -dir ./html -mkdir -split 0 $(TEX)

html: $(TEX)
	@echo "====> Generating HTML"
	$(LATEX2HTML) -dir ./html -mkdir $(TEX)

index: $(IDX)
	$(MKINDEX) $(IDX)

check: $(TEX)
	$(CHECK) $(TEX)

spell: $(TEX)
	$(SPELL) -c $(TEX)

clean:
	rm -f $(LOG) $(NAME).aux $(NAME).out $(NAME).toc
	rm -f $(DVI) $(PS) $(PDF)
	rm -f $(NAME).bbl $(NAME).blg
	rm -rf ./html
	rm -f *.lof *.lot
	rm *~
