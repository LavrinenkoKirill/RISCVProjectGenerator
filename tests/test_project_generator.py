from project_generator import *
import shlex

def test_MakeProject():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ide",type=str,help="In what IDE should the project be created",required=True, choices= {"make","vscode"})
    parser.add_argument("-s","--source", type=str, help="Source file to compile", required=True)
    parser.add_argument("-o","--output_file",type=str, help="Output file",required=True)
    parser.add_argument("--idir", type=str, help="Input directory",required=True)
    parser.add_argument("--odir", type=str, help="Output directory",required=True)
    parser.add_argument("--libc", type = str, help="Source library code file", required=False, nargs="+")
    parser.add_argument("--libh", type = str, help="Source library header file", required=False, nargs="+")
    argString = "--ide make --idir tests/riscv_make --odir tests/riscv_make -s main.c  --libc util.c --libh util.h -o edit"
    args = parser.parse_args(shlex.split(argString))
    project_generator = MakeProjectGenerator(args)
    project_generator.generateProject(args)
    flag = True
    home = os.path.expanduser("~")
    os.system("make -f " + home + args.output_dir + "/Makefile")
    if (os.listdir(home + args.output_dir + "/src") == []): flag = False
    if (os.listdir(home + args.output_dir + "/object") == []): flag = False
    if (os.listdir(home + args.output_dir + "/build") == []): flag = False
    assert flag == True

def test_VSCodeProject():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser()
    parser.add_argument("--ide",type=str,help="In what IDE should the project be created",required=True, choices= {"make","vscode"})
    parser.add_argument("-s","--source", type=str, help="Source file to compile", required=True)
    parser.add_argument("-o","--output_file",type=str, help="Output file",required=True)
    parser.add_argument("--idir", type=str, help="Input directory",required=True)
    parser.add_argument("--odir", type=str, help="Output directory",required=True)
    parser.add_argument("--libc", type = str, help="Source library code file", required=False, nargs="+")
    parser.add_argument("--libh", type = str, help="Source library header file", required=False, nargs="+")
    argString = " --ide vscode --idir /project/generator/tests/riscv_vscode --odir /project/generator/tests/riscv_vscode -s rot13.c  -o edit"
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
    parser.add_argument("--ide",type=str,help="In what IDE should the project be created",required=True, choices= {"make","vscode"})
    parser.add_argument("-s","--source", type=str, help="Source file to compile", required=True)
    parser.add_argument("-o","--output_file",type=str, help="Output file",required=True)
    parser.add_argument("--idir", type=str, help="Input directory",required=True)
    parser.add_argument("--odir", type=str, help="Output directory",required=True)
    parser.add_argument("--libc", type = str, help="Source library code file", required=False, nargs="+")
    parser.add_argument("--libh", type = str, help="Source library header file", required=False, nargs="+")
    argString = "--ide make --idir /project/generator/tests/riscv_make_debug --odir /project/generator/tests/riscv_make_debug -s one.c -o one.elf"
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
