cmake_minimum_required(VERSION 3.10)
project(test C)
set(CMAKE_C_COMPILER riscv64-unknown-elf-gcc)

SET(CRT /home/lavrinenko/project/generator/tests/riscv_vscode/bsp/crt.S)
SET(SYSCALLS /home/lavrinenko/project/generator/tests/riscv_vscode/bsp/syscalls.c)
set_property(SOURCE ${CRT} PROPERTY LANGUAGE C)


set(CRTLIB ${CRT}) 
set(SYSLIB ${SYSCALLS})


SET(LINKER_SCRIPT /home/lavrinenko/project/generator/tests/riscv_vscode/bsp/link.ld)
SET(LINKER_FLAGS "-static -nostdlib -nostartfiles -T ${LINKER_SCRIPT}")
SET(COMPILER_FLAGS "-mcmodel=medany -std=gnu99 -fno-builtin-printf -march=rv64gcv -mabi=lp64d -g")

add_library(crt STATIC ${CRTLIB})
add_library(syscalls STATIC ${SYSLIB})

string(REPLACE " " ";" COMPILER_LIST ${COMPILER_FLAGS})

target_compile_options(crt PUBLIC ${COMPILER_LIST})
target_compile_options(syscalls PUBLIC ${COMPILER_LIST})


add_executable(edit.elf /home/lavrinenko/project/generator/tests/riscv_vscode/rot13.c)
set_target_properties(edit.elf PROPERTIES LINK_DEPENDS "${LINKER_SCRIPT}")
SET(CMAKE_EXE_LINKER_FLAGS  "${LINKER_FLAGS} ${COMPILER_FLAGS}")



target_link_libraries(edit.elf crt syscalls )