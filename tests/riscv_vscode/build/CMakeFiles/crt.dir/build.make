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
include CMakeFiles/crt.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/crt.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/crt.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/crt.dir/flags.make

CMakeFiles/crt.dir/bsp/crt.S.o: CMakeFiles/crt.dir/flags.make
CMakeFiles/crt.dir/bsp/crt.S.o: ../bsp/crt.S
CMakeFiles/crt.dir/bsp/crt.S.o: CMakeFiles/crt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lavrinenko/project/generator/tests/riscv_vscode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/crt.dir/bsp/crt.S.o"
	riscv64-unknown-elf-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/crt.dir/bsp/crt.S.o -MF CMakeFiles/crt.dir/bsp/crt.S.o.d -o CMakeFiles/crt.dir/bsp/crt.S.o -c /home/lavrinenko/project/generator/tests/riscv_vscode/bsp/crt.S

CMakeFiles/crt.dir/bsp/crt.S.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/crt.dir/bsp/crt.S.i"
	riscv64-unknown-elf-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/lavrinenko/project/generator/tests/riscv_vscode/bsp/crt.S > CMakeFiles/crt.dir/bsp/crt.S.i

CMakeFiles/crt.dir/bsp/crt.S.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/crt.dir/bsp/crt.S.s"
	riscv64-unknown-elf-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/lavrinenko/project/generator/tests/riscv_vscode/bsp/crt.S -o CMakeFiles/crt.dir/bsp/crt.S.s

# Object files for target crt
crt_OBJECTS = \
"CMakeFiles/crt.dir/bsp/crt.S.o"

# External object files for target crt
crt_EXTERNAL_OBJECTS =

libcrt.a: CMakeFiles/crt.dir/bsp/crt.S.o
libcrt.a: CMakeFiles/crt.dir/build.make
libcrt.a: CMakeFiles/crt.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/lavrinenko/project/generator/tests/riscv_vscode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C static library libcrt.a"
	$(CMAKE_COMMAND) -P CMakeFiles/crt.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/crt.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/crt.dir/build: libcrt.a
.PHONY : CMakeFiles/crt.dir/build

CMakeFiles/crt.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/crt.dir/cmake_clean.cmake
.PHONY : CMakeFiles/crt.dir/clean

CMakeFiles/crt.dir/depend:
	cd /home/lavrinenko/project/generator/tests/riscv_vscode/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lavrinenko/project/generator/tests/riscv_vscode /home/lavrinenko/project/generator/tests/riscv_vscode /home/lavrinenko/project/generator/tests/riscv_vscode/build /home/lavrinenko/project/generator/tests/riscv_vscode/build /home/lavrinenko/project/generator/tests/riscv_vscode/build/CMakeFiles/crt.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/crt.dir/depend

