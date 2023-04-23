all: build/v400.pdf

build/v400.pdf: build/Brechung.pdf build/Reflexion.pdf v400.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v400.tex
	lualatex  --output-directory=build v400.tex
	biber build/v400.bcf
	lualatex  --output-directory=build v400.tex

build/Reflexion.pdf: Reflexion.txt reflexion.py | build
	python reflexion.py

build/Brechung.pdf: Brechung.txt brechung.py | build
	python brechung.py

build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
