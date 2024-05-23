generate-main:
	python3 ../project_generator.py --ide makefile --idir $(shell pwd)/main --odir $(shell pwd)/outputs/make -s main.c -o edit --libc util.c --libh util.h
	python3 ../project_generator.py --ide vscode --idir $(shell pwd)/main --odir $(shell pwd)/outputs/vscode -s main.c -o edit --libc util.c --libh util.h

build-main:
	make -C outputs/ build-make
	make -C outputs/ build-vscode


