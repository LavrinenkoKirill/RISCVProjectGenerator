#!/bin/bash
xterm -e spike --rbb-port=9824 -H /home/lavrinenko/project/generator/test_projects/outputs/make/build/edit &
sleep 1
xterm -e openocd -f /home/lavrinenko/project/generator/test_projects/outputs/make/spike.cfg &
sleep 1
riscv-none-elf-gdb -x commands.txt --args /home/lavrinenko/project/generator/test_projects/outputs/make/build/edit