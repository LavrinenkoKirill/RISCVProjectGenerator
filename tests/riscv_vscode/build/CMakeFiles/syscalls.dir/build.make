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
include CMakeFiles/syscalls.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/syscalls.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/syscalls.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/syscalls.dir/flags.make

CMakeFiles/syscalls.dir/bsp/syscalls.c.o: CMakeFiles/syscalls.dir/flags.make
CMakeFiles/syscalls.dir/bsp/syscalls.c.o: ../bsp/syscalls.c
CMakeFiles/syscalls.dir/bsp/syscalls.c.o: CMakeFiles/syscalls.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lavrinenko/project/generator/tests/riscv_vscode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/syscalls.dir/bsp/syscalls.c.o"
	riscv64-unknown-elf-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/syscalls.dir/bsp/syscalls.c.o -MF CMakeFiles/syscalls.dir/bsp/syscalls.c.o.d -o CMakeFiles/syscalls.dir/bsp/syscalls.c.o -c /home/lavrinenko/project/generator/tests/riscv_vscode/bsp/syscalls.c

CMakeFiles/syscalls.dir/bsp/syscalls.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/syscalls.dir/bsp/syscalls.c.i"
	riscv64-unknown-elf-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/lavrinenko/project/generator/tests/riscv_vscode/bsp/syscalls.c > CMakeFiles/syscalls.dir/bsp/syscalls.c.i

CMakeFiles/syscalls.dir/bsp/syscalls.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/syscalls.dir/bsp/syscalls.c.s"
	riscv64-unknown-elf-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/lavrinenko/project/generator/tests/riscv_vscode/bsp/syscalls.c -o CMakeFiles/syscalls.dir/bsp/syscalls.c.s

# Object files for target syscalls
syscalls_OBJECTS = \
"CMakeFiles/syscalls.dir/bsp/syscalls.c.o"

# External object files for target syscalls
syscalls_EXTERNAL_OBJECTS =

libsyscalls.a: CMakeFiles/syscalls.dir/bsp/syscalls.c.o
libsyscalls.a: CMakeFiles/syscalls.dir/build.make
libsyscalls.a: CMakeFiles/syscalls.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/lavrinenko/project/generator/tests/riscv_vscode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C static library libsyscalls.a"
	$(CMAKE_COMMAND) -P CMakeFiles/syscalls.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/syscalls.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/syscalls.dir/build: libsyscalls.a
.PHONY : CMakeFiles/syscalls.dir/build

CMakeFiles/syscalls.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/syscalls.dir/cmake_clean.cmake
.PHONY : CMakeFiles/syscalls.dir/clean

CMakeFiles/syscalls.dir/depend:
	cd /home/lavrinenko/project/generator/tests/riscv_vscode/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lavrinenko/project/generator/tests/riscv_vscode /home/lavrinenko/project/generator/tests/riscv_vscode /home/lavrinenko/project/generator/tests/riscv_vscode/build /home/lavrinenko/project/generator/tests/riscv_vscode/build /home/lavrinenko/project/generator/tests/riscv_vscode/build/CMakeFiles/syscalls.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/syscalls.dir/depend
