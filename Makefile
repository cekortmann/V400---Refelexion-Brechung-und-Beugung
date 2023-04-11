all: build/v400.pdf

build/v400.pdf: v400.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v400.tex
	lualatex  --output-directory=build v400.tex
	biber build/v400.bcf
	lualatex  --output-directory=build v400.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
