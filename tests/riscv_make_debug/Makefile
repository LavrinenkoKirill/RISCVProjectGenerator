PREFIX = .
SRC = $(wildcard $(PREFIX)/bsp/*.c)\
	$(wildcard $(PREFIX)/bsp/*.S)
	
OBJ = $(addsuffix .o, $(basename $(notdir $(SRC))))

GCC = riscv64-unknown-elf-gcc
COMPILER_FLAGS = -mcmodel=medany -std=gnu99 -fno-builtin-printf -march=rv64gcv -mabi=lp64d -g 
LINKER_FLAGS = -static -nostdlib -nostartfiles -T $(PREFIX)/bsp/link.ld

/home/lavrinenko/project/generator/tests/riscv_make_debug/build/one.elf: /home/lavrinenko/project/generator/tests/riscv_make_debug/object/one.o  $(OBJ)
	$(GCC) -o /home/lavrinenko/project/generator/tests/riscv_make_debug/build/one.elf /home/lavrinenko/project/generator/tests/riscv_make_debug/object/one.o  $(OBJ) $(LINKER_FLAGS)
	
$(OBJ): $(SRC)
	$(GCC) $(COMPILER_FLAGS) -c $(SRC)

/home/lavrinenko/project/generator/tests/riscv_make_debug/object/one.o: /home/lavrinenko/project/generator/tests/riscv_make_debug/one.c 
	$(GCC) -c /home/lavrinenko/project/generator/tests/riscv_make_debug/one.c -o /home/lavrinenko/project/generator/tests/riscv_make_debug/object/one.o $(COMPILER_FLAGS)
