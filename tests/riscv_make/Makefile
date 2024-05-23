PREFIX = .
SRC = $(wildcard $(PREFIX)/bsp/*.c)\
	$(wildcard $(PREFIX)/bsp/*.S)
	
OBJ = $(addsuffix .o, $(basename $(notdir $(SRC))))

GCC = riscv64-unknown-elf-gcc
COMPILER_FLAGS = -mcmodel=medany -std=gnu99 -fno-builtin-printf -march=rv64gcv -mabi=lp64d -g 
LINKER_FLAGS = -static -nostdlib -nostartfiles -T $(PREFIX)/bsp/link.ld

/home/lavrinenko/project/generator/tests/riscv_make/build/edit: /home/lavrinenko/project/generator/tests/riscv_make/object/main.o /home/lavrinenko/project/generator/tests/riscv_make/object/util.o $(OBJ)
	$(GCC) -o /home/lavrinenko/project/generator/tests/riscv_make/build/edit /home/lavrinenko/project/generator/tests/riscv_make/object/main.o /home/lavrinenko/project/generator/tests/riscv_make/object/util.o $(OBJ) $(LINKER_FLAGS)
	
$(OBJ): $(SRC)
	$(GCC) $(COMPILER_FLAGS) -c $(SRC)

/home/lavrinenko/project/generator/tests/riscv_make/object/main.o: /home/lavrinenko/project/generator/tests/riscv_make/main.c /home/lavrinenko/project/generator/tests/riscv_make/util.h
	$(GCC) -c /home/lavrinenko/project/generator/tests/riscv_make/main.c -o /home/lavrinenko/project/generator/tests/riscv_make/object/main.o $(COMPILER_FLAGS)
/home/lavrinenko/project/generator/tests/riscv_make/object/util.o : /home/lavrinenko/project/generator/tests/riscv_make/util.c /home/lavrinenko/project/generator/tests/riscv_make/util.h
	riscv64-unknown-elf-gcc -o /home/lavrinenko/project/generator/tests/riscv_make/object/util.o -c /home/lavrinenko/project/generator/tests/riscv_make/util.c $(COMPILER_FLAGS)