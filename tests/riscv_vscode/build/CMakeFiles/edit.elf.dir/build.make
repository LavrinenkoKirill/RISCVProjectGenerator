# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/lavrinenko/project/generator/tests/riscv_vscode

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/lavrinenko/project/generator/tests/riscv_vscode/build

# Include any dependencies generated for this target.
include CMakeFiles/edit.elf.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/edit.elf.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/edit.elf.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/edit.elf.dir/flags.make

CMakeFiles/edit.elf.dir/rot13.c.o: CMakeFiles/edit.elf.dir/flags.make
CMakeFiles/edit.elf.dir/rot13.c.o: ../rot13.c
CMakeFiles/edit.elf.dir/rot13.c.o: CMakeFiles/edit.elf.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lavrinenko/project/generator/tests/riscv_vscode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/edit.elf.dir/rot13.c.o"
	riscv64-unknown-elf-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/edit.elf.dir/rot13.c.o -MF CMakeFiles/edit.elf.dir/rot13.c.o.d -o CMakeFiles/edit.elf.dir/rot13.c.o -c /home/lavrinenko/project/generator/tests/riscv_vscode/rot13.c

CMakeFiles/edit.elf.dir/rot13.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/edit.elf.dir/rot13.c.i"
	riscv64-unknown-elf-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/lavrinenko/project/generator/tests/riscv_vscode/rot13.c > CMakeFiles/edit.elf.dir/rot13.c.i

CMakeFiles/edit.elf.dir/rot13.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/edit.elf.dir/rot13.c.s"
	riscv64-unknown-elf-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/lavrinenko/project/generator/tests/riscv_vscode/rot13.c -o CMakeFiles/edit.elf.dir/rot13.c.s

# Object files for target edit.elf
edit_elf_OBJECTS = \
"CMakeFiles/edit.elf.dir/rot13.c.o"

# External object files for target edit.elf
edit_elf_EXTERNAL_OBJECTS =

edit.elf: CMakeFiles/edit.elf.dir/rot13.c.o
edit.elf: CMakeFiles/edit.elf.dir/build.make
edit.elf: libcrt.a
edit.elf: libsyscalls.a
edit.elf: ../bsp/link.ld
edit.elf: CMakeFiles/edit.elf.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/lavrinenko/project/generator/tests/riscv_vscode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable edit.elf"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/edit.elf.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/edit.elf.dir/build: edit.elf
.PHONY : CMakeFiles/edit.elf.dir/build

CMakeFiles/edit.elf.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/edit.elf.dir/cmake_clean.cmake
.PHONY : CMakeFiles/edit.elf.dir/clean

CMakeFiles/edit.elf.dir/depend:
	cd /home/lavrinenko/project/generator/tests/riscv_vscode/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lavrinenko/project/generator/tests/riscv_vscode /home/lavrinenko/project/generator/tests/riscv_vscode /home/lavrinenko/project/generator/tests/riscv_vscode/build /home/lavrinenko/project/generator/tests/riscv_vscode/build /home/lavrinenko/project/generator/tests/riscv_vscode/build/CMakeFiles/edit.elf.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/edit.elf.dir/depend

