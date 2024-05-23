PREFIX = .
SRC = $(wildcard $(PREFIX)/bsp/*.c)\
	$(wildcard $(PREFIX)/bsp/*.S)
	
OBJ = $(addprefix object/, $(addsuffix .o, $(basename $(notdir $(SRC)))))

GCC = riscv64-unknown-elf-gcc
COMPILER_FLAGS = -mcmodel=medany -std=gnu99 -fno-builtin-printf -march=rv64gcv -mabi=lp64d -g
LINKER_FLAGS = -static -nostdlib -nostartfiles -T $(PREFIX)/bsp/link.ld

/home/lavrinenko/project/generator/test_projects/outputs/make/build/edit: /home/lavrinenko/project/generator/test_projects/outputs/make/object/main.o /home/lavrinenko/project/generator/test_projects/outputs/make/object/util.o $(OBJ)
	$(GCC) -o /home/lavrinenko/project/generator/test_projects/outputs/make/build/edit /home/lavrinenko/project/generator/test_projects/outputs/make/object/main.o /home/lavrinenko/project/generator/test_projects/outputs/make/object/util.o $(OBJ) $(LINKER_FLAGS)
	
$(OBJ): $(SRC)
	cd object/ && $(GCC) $(COMPILER_FLAGS) -c $(addprefix ../, $(SRC))

/home/lavrinenko/project/generator/test_projects/outputs/make/object/main.o: /home/lavrinenko/project/generator/test_projects/outputs/make/main.c /home/lavrinenko/project/generator/test_projects/main/util.h
	$(GCC) -c /home/lavrinenko/project/generator/test_projects/outputs/make/main.c -o /home/lavrinenko/project/generator/test_projects/outputs/make/object/main.o $(COMPILER_FLAGS)
/home/lavrinenko/project/generator/test_projects/outputs/make/object/util.o : /home/lavrinenko/project/generator/test_projects/outputs/make/util.c /home/lavrinenko/project/generator/test_projects/main/util.h
	riscv64-unknown-elf-gcc -o /home/lavrinenko/project/generator/test_projects/outputs/make/object/util.o -c /home/lavrinenko/project/generator/test_projects/outputs/make/util.c $(COMPILER_FLAGS)