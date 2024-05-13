import os
from jinja2 import Environment,FileSystemLoader,Template
import argparse
import shutil
import sys


class ProjectGenerator:
    def __init__(self,args):
        self.source_path = args.input_dir + '/' + args.source
        self.output_path = args.output_dir + "/build/" + args.output_file
        self.obj_main_path = args.output_dir + "/object/" + args.source.replace(".c",".o")
        if (args.library_source):
            self.obj_lib_path = [None] * len(args.library_source) 
            for n in range(len(args.library_source)):
                self.obj_lib_path[n] = args.output_dir + "/object/" + args.library_source[n].replace(".c",".o")
        else: self.obj_lib_path = ""
        if (args.library_header):
            self.header_lib_path = [None] * len(args.library_header)
            for (n) in range(len(args.library_header)): 
                self.header_lib_path[n] = args.input_dir + '/' + args.library_header[n]
        else: self.header_lib_path = ""
        self.cflags_str = ""
        if (args.cflags) : 
            for n in range(len(args.cflags)):
                self.cflags_str += '-' + args.cflags[n]+' '
        
        self.ldflags_str = ""
        home = os.path.expanduser("~")
        if (args.ldflag) : 
            self.ldflags_str += '-T ' + home + args.input_dir + '/' + args.ldflag + ' -nostartfiles'

    
    def createFolders(self,args):
        home = os.path.expanduser("~")
        if (os.path.isdir(home + args.output_dir + "/build") == False): os.mkdir(home + args.output_dir + "/build")
        if (args.ide == "make"):
            if (os.path.isdir(home + args.output_dir + "/object") == False): os.mkdir(home + args.output_dir + "/object")
        if (args.library_header):
            if (os.path.isdir(home + args.output_dir + "/headers") == False): os.mkdir(home + args.output_dir + "/headers")
        if (args.ldflag):
            if (os.path.isdir(home + args.output_dir + "/bsp") == False):os.mkdir(home + args.output_dir + "/bsp")
        if (os.path.isdir(home + args.output_dir + "/src") == False): os.mkdir(home + args.output_dir + "/src")

    def copyFiles(self,args):
        home = os.path.expanduser("~")
        if (args.library_header):
            for (n) in range(len(args.library_header)): 
                shutil.copy(home + self.header_lib_path[n],home + args.output_dir + "/headers/" + args.library_header[n])

        if (args.ldflag) : 
            shutil.copy(home + args.input_dir + '/' + args.ldflag, home + args.output_dir + "/bsp/" + args.ldflag)
        
        shutil.copy(home + self.source_path, home + args.output_dir + "/src/" + args.source)

        if (args.openocd): shutil.copy(home + args.input_dir + '/' + args.openocd, home + args.output_dir + "/bsp/" + args.openocd)

        if (args.library_source):
            for i in range (len(args.library_source)):
                shutil.copy(home + args.input_dir + '/' + args.library_source[i], home + args.output_dir + "/src/" + args.library_source[i])

class MakeProjectGenerator(ProjectGenerator):
    def __init__(self,args):
        super().__init__(args)
        file_loader = FileSystemLoader('templates')
        env = Environment(loader = file_loader)
        self.template = env.get_template('Makefile.template')
        if (args.openocd): self.openocd = args.output_dir + "/bsp/" + args.openocd
    
    def createDebugScripts(self,args):
        home = os.path.expanduser("~")
        bash_templates_loader = FileSystemLoader('templates/bash_templates')
        env = Environment(loader = bash_templates_loader)
        tm = env.get_template('start_debug.template')
        result = tm.render(executable = home + self.output_path, openocd_cfg = home + self.openocd)
        f = open(home + args.output_dir + "/start_debug.sh","w")
        f.write(result)
        shutil.copy("templates/bash_templates/end_debug.sh",home + args.output_dir + "/end_debug.sh")

    def generateProject(self,args):
        home = os.path.expanduser("~")
        super().createFolders(args)
        super().copyFiles(args)
        object_str = ""
        if (args.library_source): object_str = home + str(self.obj_lib_path)[2:-2]
        header_str = ""
        if (args.library_header): header_str = home + str(self.header_lib_path)[2:-2]

        result = self.template.render(source = home + self.source_path
                       , output = home + self.output_path
                       , main_obj = home + self.obj_main_path
                       , lib_obj = object_str
                       , lib_h = header_str
                       , cflags = self.cflags_str
                       , ldflags = self.ldflags_str)
        f = open(home + args.output_dir + "/Makefile","w")
        f.write(result)

        if (args.library_source):
            libc_path = [None] * len(args.library_source)
            for n in range (len(args.library_source)):
                libc_path[n] = home + args.input_dir + '/' + args.library_source[n] 


        if (args.library_source):
            for n in range (len(args.library_source)):
                obj_string = home + self.obj_lib_path[n] + ' : ' + home + args.input_dir + '/' + args.library_source[n] + " " + home + self.header_lib_path[n]
                f.write(obj_string)
                f.write('\n')
                f.write('\t' + "riscv64-unknown-elf-gcc -o " + home + self.obj_lib_path[n] + " -c " + libc_path[n])
        f.close()

        if (args.openocd): self.createDebugScripts(args)


class VSCodeGenerator(ProjectGenerator):
    def __init__(self,args):
        super().__init__(args)
        home = os.path.expanduser("~")
        file_loader = FileSystemLoader('templates')
        env = Environment(loader = file_loader)
        self.template = env.get_template('CMakeLists.template')
        self.vsfolder = args.output_dir + "/.vscode"
        self.output_path = args.output_file
        f = open(home + args.input_dir + '/' + args.config,"r")
        for line in f:
            if ("compilerPath" in line):
                index = line.find(":")
                self.compiler_path = line[index + 2:-1]
            elif ("gdbPath" in line):
                index = line.find(":")
                self.gdb_path = line[index + 2:-1]
            elif ("spikePath" in line):
                index = line.find(":")
                self.spike_path = line[index + 2:-1]
            elif ("openocdPath" in line):
                index = line.find(":")
                self.openocd_path = line[index + 2:-1]
            

    
    def createFolders(self,args):
        super().createFolders(args)
        home = os.path.expanduser("~")
        if (os.path.isdir(home + self.vsfolder) == False): os.mkdir(home + self.vsfolder)
    
    def copyFiles(self, args):
        super().copyFiles(args)
        home = os.path.expanduser("~")
        vs_templates_loader = FileSystemLoader('templates/vscode_templates')
        env = Environment(loader = vs_templates_loader)
        tm = env.get_template('launch.template')
        result = tm.render(output = home + args.output_dir + "/build/" + args.output_file,
                           gdb = self.gdb_path)
        launch_file = open(home + args.output_dir + "/.vscode/launch.json","w")
        launch_file.write(result)
        launch_file.close()


        tm = env.get_template("c_cpp_properties.template")
        result = tm.render(compiler = self.compiler_path)
        cpp_file = open(home + args.output_dir + "/.vscode/c_cpp_properties.json","w")
        cpp_file.write(result)
        cpp_file.close()

        shutil.copy(home + "/project/generator/templates/vscode_templates/settings.json",home + args.output_dir + "/.vscode/settings.json")

        tm = env.get_template('tasks.template')
        shutil.copy(home + args.input_dir + '/' + args.openocd, home + args.output_dir + "/bsp/" + args.openocd)
        result = tm.render(output = home + args.output_dir + "/build/" + args.output_file, openocd_cfg = home + args.output_dir + "/bsp/" + args.openocd,
                           openocd = self.openocd_path,
                           spike  = self.spike_path)
        tasks_file = open(home + args.output_dir + "/.vscode/tasks.json","w")
        tasks_file.write(result)
        tasks_file.close()

    def generateProject(self,args):
        self.createFolders(args)
        self.copyFiles(args)
        home = os.path.expanduser("~")
        result = self.template.render(source = home + self.source_path
                       , output = self.output_path
                       , cflags = self.cflags_str
                       , linker_script = home + args.input_dir + '/' + args.ldflag)
        f = open(home + args.output_dir + '/' + "CMakeLists.txt","w")
        f.write(result)
        f.close()


def parseArguments():
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
    return parser.parse_args()

if (len(sys.argv)> 1):
    args = parseArguments()

    if (args.ide == "make"):
        project_generator = MakeProjectGenerator(args)
        project_generator.generateProject(args)

    elif (args.ide == "vscode"):
        project_generator = VSCodeGenerator(args)
        project_generator.generateProject(args)

    else: print("Not supported")






