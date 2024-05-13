from project_generator import *
import shlex

def test_MakeProject():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ide",type=str,help="In what IDE should the project be created",required=True, choices= {"make","vscode"})
    parser.add_argument("-s","--source", type=str, help="Source file to compile", required=True)
    parser.add_argument("-o","--output_file",type=str, help="Output file",required=True)
    parser.add_argument("-idir", "--input_dir", type=str, help="Input directory",required=True)
    parser.add_argument("-odir", "--output_dir", type=str, help="Output directory",required=True)
    parser.add_argument("-libc", "--library_source", type = str, help="Source library code file", required=False, nargs="+")
    parser.add_argument("-libh", "--library_header", type = str, help="Source library header file", required=False, nargs="+")
    parser.add_argument("--cflags",type = str, help="Flags for compilation", required=False, nargs="+")
    parser.add_argument("--ldflag", type = str, help = "Flag for linker script", required=False)
    parser.add_argument("--openocd", type = str, help = "OpenOCD configuration", required = False)
    parser.add_argument("--config", type = str, help = "Compiler,GDB and Openocd configuration", required=False)
    argString = "-ide make -idir /project/generator/tests/riscv_make -odir /project/generator/tests/riscv_make -s main.c  -libc util.c -libh util.h -o edit --cflags g"
    args = parser.parse_args(shlex.split(argString))
    project_generator = MakeProjectGenerator(args)
    project_generator.generateProject(args)
    flag = True
    home = os.path.expanduser("~")
    os.system("make -f " + home + args.output_dir + "/Makefile")
    if (os.listdir(home + args.output_dir + "/src") == []): flag = False
    if (os.listdir(home + args.output_dir + "/headers") == []): flag = False
    if (os.listdir(home + args.output_dir + "/object") == []): flag = False
    if (os.listdir(home + args.output_dir + "/build") == []): flag = False
    assert flag == True

def test_VSCodeProject():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ide",type=str,help="In what IDE should the project be created",required=True, choices= {"make","vscode"})
    parser.add_argument("-s","--source", type=str, help="Source file to compile", required=True)
    parser.add_argument("-o","--output_file",type=str, help="Output file",required=True)
    parser.add_argument("-idir", "--input_dir", type=str, help="Input directory",required=True)
    parser.add_argument("-odir", "--output_dir", type=str, help="Output directory",required=True)
    parser.add_argument("-libc", "--library_source", type = str, help="Source library code file", required=False, nargs="+")
    parser.add_argument("-libh", "--library_header", type = str, help="Source library header file", required=False, nargs="+")
    parser.add_argument("--cflags",type = str, help="Flags for compilation", required=False, nargs="+")
    parser.add_argument("--ldflag", type = str, help = "Flag for linker script", required=False)
    parser.add_argument("--openocd", type = str, help = "OpenOCD configuration", required = False)
    parser.add_argument("--config", type = str, help = "Compiler,GDB and Openocd configuration", required=False)
    argString = " -ide vscode -idir /project/generator/tests/riscv_vscode -odir /project/generator/tests/riscv_vscode -s rot13.c  -o edit.elf --cflags g Og --ldflag spike.lds --openocd spike.cfg --config generator.cfg"
    args = parser.parse_args(shlex.split(argString))
    project_generator = VSCodeGenerator(args)
    project_generator.generateProject(args)

    flag = True
    home = os.path.expanduser("~")
    if (os.listdir(home + args.output_dir + "/src") == []): flag = False
    if (os.listdir(home + args.output_dir + "/.vscode") == []): flag = False
    if (os.path.isfile(home + args.output_dir + "/CMakeLists.txt") == False): flag = False
    assert flag == True
    

def testMakeProjectDebug():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ide",type=str,help="In what IDE should the project be created",required=True, choices= {"make","vscode"})
    parser.add_argument("-s","--source", type=str, help="Source file to compile", required=True)
    parser.add_argument("-o","--output_file",type=str, help="Output file",required=True)
    parser.add_argument("-idir", "--input_dir", type=str, help="Input directory",required=True)
    parser.add_argument("-odir", "--output_dir", type=str, help="Output directory",required=True)
    parser.add_argument("-libc", "--library_source", type = str, help="Source library code file", required=False, nargs="+")
    parser.add_argument("-libh", "--library_header", type = str, help="Source library header file", required=False, nargs="+")
    parser.add_argument("--cflags",type = str, help="Flags for compilation", required=False, nargs="+")
    parser.add_argument("--ldflag", type = str, help = "Flag for linker script", required=False)
    parser.add_argument("--openocd", type = str, help = "OpenOCD configuration", required = False)
    parser.add_argument("--config", type = str, help = "Compiler,GDB and Openocd configuration", required=False)
    argString = "-ide make -idir /project/generator/tests/riscv_make_debug -odir /project/generator/tests/riscv_make_debug -s one.c -o one.elf --cflags g Og  --ldflag spike.lds --openocd spike.cfg"
    args = parser.parse_args(shlex.split(argString))
    project_generator = MakeProjectGenerator(args)
    project_generator.generateProject(args)
    flag = True
    home = os.path.expanduser("~")
    os.system("make -f " + home + args.output_dir + "/Makefile")
    if (os.listdir(home + args.output_dir + "/src") == []): flag = False
    if (os.listdir(home + args.output_dir + "/object") == []): flag = False
    if (os.listdir(home + args.output_dir + "/build") == []): flag = False
    if (os.path.isfile(home + args.output_dir + "/start_debug.sh") == False): flag = False
    if (os.path.isfile(home + args.output_dir + "/end_debug.sh") == False): flag = False
    assert flag == True
