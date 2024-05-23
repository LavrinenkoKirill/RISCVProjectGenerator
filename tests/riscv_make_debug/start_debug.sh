#!/bin/bash
xterm -e spike --rbb-port=9824 /home/lavrinenko/project/generator/tests/riscv_make_debug/build/one.elf &
sleep 1
xterm -e openocd -f /home/lavrinenko/project/generator/tests/riscv_make_debug/bsp/spike.cfg &
sleep 1
riscv-none-elf-gdb /home/lavrinenko/project/generator/tests/riscv_make_debug/build/one.elf