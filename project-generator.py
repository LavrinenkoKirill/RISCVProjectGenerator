import os
from jinja2 import Environment,FileSystemLoader,Template
import argparse
import shutil


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

args = parser.parse_args()


def create_makefile_project(args):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader = file_loader)
    tm = env.get_template('Makefile.template')
    source_path = args.input_dir + '/' + args.source
    if (args.library_source):
        libc_path = [None] * len(args.library_source)
        for n in range (len(args.library_source)):
            libc_path[n] = args.input_dir + '/' + args.library_source[n]     
    if (os.path.isdir(args.output_dir + "/build") == False): os.mkdir(args.output_dir + "/build")
    output_path = args.output_dir + "/build/" + args.output_file
    if (os.path.isdir(args.output_dir + "/object") == False): os.mkdir(args.output_dir + "/object")
    obj_main_path = args.output_dir + "/object/" + args.source.replace(".c",".o")
    
    if (args.library_source):
        obj_lib_path = [None] * len(args.library_source) 
        for n in range(len(args.library_source)):
            obj_lib_path[n] = args.output_dir + "/object/" + args.library_source[n].replace(".c",".o")
    else: obj_lib_path = ""
    
    if (args.library_header):
        if (os.path.isdir(args.output_dir + "/headers") == False): os.mkdir(args.output_dir + "/headers")
        header_lib_path = [None] * len(args.library_header)
        for (n) in range(len(args.library_header)): 
            header_lib_path[n] = args.input_dir + '/' + args.library_header[n]
            shutil.copy(header_lib_path[n],args.output_dir + "/headers/" + args.library_header[n])
    else: header_lib_path = ""
    cflags_str = ""
    if (args.cflags) : 
        for n in range(len(args.cflags)):
            cflags_str += '-' + args.cflags[n]+' '
    ldflags_str = ""
    if (args.ldflag) : 
        if (os.path.isdir(args.output_dir + "/bsp") == False):os.mkdir(args.output_dir + "/bsp")
        shutil.copy(args.input_dir + '/' + args.ldflag, args.output_dir + "/bsp/" + args.ldflag)
        ldflags_str += '-T ' + args.input_dir + '/' + args.ldflag + ' -nostartfiles'

    if(os.path.isdir(args.output_dir + "/src") == False): os.mkdir(args.output_dir + "/src")
    shutil.copy(args.input_dir + '/' + args.source, args.output_dir + "/src/" + args.source)
    if (args.library_source):
        for i in range (len(args.library_source)):
            shutil.copy(args.input_dir + '/' + args.library_source[i], args.output_dir + "/src/" + args.library_source[i])

    result = tm.render(source = source_path
                       , output = output_path
                       , main_obj = obj_main_path
                       , lib_obj = str(obj_lib_path)[2:-2]
                       , lib_h = str(header_lib_path)[2:-2]
                       , cflags = cflags_str
                       , ldflags = ldflags_str)

    f = open(args.output_dir + "/Makefile","w")
    f.write(result)
    if (args.library_source):
        for n in range (len(args.library_source)):
            obj_string = obj_lib_path[n] + ' : ' + args.input_dir + '/' + args.library_source[n] + " " + header_lib_path[n]
            f.write(obj_string)
            f.write('\n')
            f.write('\t' + "riscv64-unknown-elf-gcc -o " + obj_lib_path[n] + " -c " + libc_path[n])
    f.close()
    os.system("make -f " + args.output_dir + "/Makefile")

def create_vscode_project(args):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader = file_loader)
    tm = env.get_template('CMakeLists.template')
    source_path = args.input_dir + '/' + args.source
    if (os.path.isdir(args.output_dir + "/build") == False): os.mkdir(args.output_dir + "/build")
    output_path = args.output_file
    cflags_str=""
    if (args.cflags) : 
        for n in range(len(args.cflags)):
            cflags_str +=  '-' + args.cflags[n]+ ' '
    ldflags_str = ""
    if (args.ldflag) : 
        if (os.path.isdir(args.output_dir + "/bsp") == False): os.mkdir(args.output_dir + "/bsp")
        shutil.copy(args.input_dir + '/' + args.ldflag, args.output_dir + "/bsp/" + args.ldflag)
        ldflags_str += '-T ' + args.input_dir + '/' + args.ldflag + ' '
    result = tm.render(  source = source_path
                       , output = output_path
                       , cflags = cflags_str
                       , linker_script = args.input_dir + '/' + args.ldflag)
    f = open( args.output_dir + '/' + "CMakeLists.txt","w")
    f.write(result)
    f.close()
    if (os.path.isdir(args.output_dir + "/.vscode") == False): os.mkdir(args.output_dir + "/.vscode")
    shutil.copy("/home/lavrinenko/project/generator/templates/vscode_templates/c_cpp_properties.json",args.output_dir + "/.vscode/c_cpp_properties.json")
    shutil.copy("/home/lavrinenko/project/generator/templates/vscode_templates/settings.json",args.output_dir + "/.vscode/settings.json")
    vs_templates_loader = FileSystemLoader('templates/vscode_templates')
    env = Environment(loader = vs_templates_loader)
    tm = env.get_template('launch.template')
    result = tm.render(output = args.output_dir + "/build/" + args.output_file)
    launch_file = open(args.output_dir + "/.vscode/launch.json","w")
    launch_file.write(result)
    launch_file.close()

    tm = env.get_template('tasks.template')
    shutil.copy(args.input_dir + '/' + args.openocd, args.output_dir + "/bsp/" + args.openocd)
    result = tm.render(output = args.output_dir + "/build/" + args.output_file, openocd_cfg = args.output_dir + "/bsp/" + args.openocd)
    tasks_file = open(args.output_dir + "/.vscode/tasks.json","w")
    tasks_file.write(result)
    tasks_file.close()
    if (os.path.isdir(args.output_dir + "/src") == False): os.mkdir(args.output_dir + "/src")
    shutil.copy(args.input_dir + '/' + args.source, args.output_dir + "/src/" + args.source)
    if (args.library_source):
        for i in range (len(args.library_source)):
            shutil.copy(args.input_dir + '/' + args.library_source[i], args.output_dir + "/src/" + args.library_source[i])



if (args.ide == "make"):
    create_makefile_project(args)

elif (args.ide == "vscode"):
    create_vscode_project(args)

else: print("Not supported")

