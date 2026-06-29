PDF=main.pdf
all:
	latexmk -pdf main.tex
clean:
	latexmk -C
