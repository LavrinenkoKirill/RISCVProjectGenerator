import os
from jinja2 import Environment,FileSystemLoader,Template
import argparse
import shutil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class ProjectGenerator:
    def __init__(self,args):
        self.source_path = args.idir + '/' + args.source
        self.output_path = args.odir + "/build/" + args.output_file
        self.obj_main_path = args.odir + "/object/" + args.source.replace(".c",".o")
        if (args.libc):
            self.obj_lib_path = [None] * len(args.libc) 
            for n in range(len(args.libc)):
                self.obj_lib_path[n] = args.odir + "/object/" + args.libc[n].replace(".c",".o")
        else: self.obj_lib_path = ""
        if (args.libh):
            self.header_lib_path = [None] * len(args.libh)
            for (n) in range(len(args.libh)): 
                self.header_lib_path[n] = args.idir + '/' + args.libh[n]
        else: self.header_lib_path = ""
        

    
    def createFolders(self,args):
        if (os.path.isdir(args.odir + "/build") == False): os.mkdir(args.odir + "/build")
        if (args.ide == "makefile"):
            if (os.path.isdir(args.odir + "/object") == False): os.mkdir(args.odir + "/object")

    def copyFiles(self,args):
        if (args.libh):
            for (n) in range(len(args.libh)): 
                shutil.copy(self.header_lib_path[n],args.odir + '/' + args.libh[n])
        
        shutil.copy(self.source_path,args.odir + '/' + args.source)
        if (os.path.isdir(args.odir + "/bsp") == False):shutil.copytree(ROOT_DIR + "/bsp",args.odir + "/bsp")
        if (os.path.isfile(args.odir + "/spike.cfg") == False):shutil.copy(ROOT_DIR + "/templates/spike.cfg",args.odir + "/spike.cfg")

        if (args.libc):
            for i in range (len(args.libc)):
                shutil.copy(args.idir + '/' + args.libc[i],args.odir + '/' + args.libc[i])

class MakeProjectGenerator(ProjectGenerator):
    def __init__(self,args):
        super().__init__(args)
        file_loader = FileSystemLoader(ROOT_DIR + '/templates')
        env = Environment(loader = file_loader)
        self.template = env.get_template('Makefile.template')
        self.openocd = args.odir + "/spike.cfg"
        
    
    def createDebugScripts(self,args):
        bash_templates_loader = FileSystemLoader(ROOT_DIR + '/templates/bash')
        env = Environment(loader = bash_templates_loader)
        tm = env.get_template('start_debug.template')
        result = tm.render(executable = self.output_path, openocd_cfg = self.openocd)
        f = open(args.odir + "/start_debug.sh","w")
        f.write(result)
        shutil.copy(ROOT_DIR + "/templates/bash/end_debug.sh",args.odir + "/end_debug.sh")
        shutil.copy(ROOT_DIR + "/templates/bash/commands.txt",args.odir + "/commands.txt")

    def generateProject(self,args):
        super().createFolders(args)
        super().copyFiles(args)
        object_str = ""
        if (args.libc): object_str = str(self.obj_lib_path)[2:-2]
        header_str = ""
        if (args.libh): header_str = str(self.header_lib_path)[2:-2]

        result = self.template.render(source = args.odir + '/' + args.source
                       , output = self.output_path
                       , main_obj = self.obj_main_path
                       , lib_obj = object_str
                       , lib_h = header_str)
        f = open(args.odir + "/Makefile","w")
        f.write(result)

        if (args.libc):
            libc_path = [None] * len(args.libc)
            for n in range (len(args.libc)):
                libc_path[n] = args.odir + '/' + args.libc[n] 


        if (args.libc):
            for n in range (len(args.libc)):
                obj_string = self.obj_lib_path[n] + ' : ' + args.odir + '/' + args.libc[n] + " " + self.header_lib_path[n]
                f.write(obj_string)
                f.write('\n')
                f.write('\t' + "riscv64-unknown-elf-gcc -o " + self.obj_lib_path[n] + " -c " + libc_path[n] + " $(COMPILER_FLAGS)")
        f.close()

        self.createDebugScripts(args)


class VSCodeGenerator(ProjectGenerator):
    def __init__(self,args):
        super().__init__(args)
        file_loader = FileSystemLoader(ROOT_DIR + '/templates')
        env = Environment(loader = file_loader)
        self.template = env.get_template('CMakeLists.template')
        self.vsfolder = args.odir + "/.vscode"
        self.output_path = args.output_file
        f = open(ROOT_DIR + "/config.yaml","r")
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
        
        if (args.libc):
            self.output_lib_path = [None] * len(args.libc)
            for (n) in range(len(args.libc)): 
                self.output_lib_path[n] = args.odir + '/' + args.libc[n]
        else: self.output_lib_path = ""
            

    
    def createFolders(self,args):
        super().createFolders(args)
        if (os.path.isdir(self.vsfolder) == False): os.mkdir(self.vsfolder)
    
    def copyFiles(self, args):
        super().copyFiles(args)
        vs_templates_loader = FileSystemLoader(ROOT_DIR + '/templates/vscode')
        env = Environment(loader = vs_templates_loader)
        tm = env.get_template('launch.template')
        result = tm.render(output = args.odir + "/build/" + args.output_file,
                           gdb = self.gdb_path)
        launch_file = open(args.odir + "/.vscode/launch.json","w")
        launch_file.write(result)
        launch_file.close()

        tm = env.get_template("c_cpp_properties.template")
        result = tm.render(compiler = self.compiler_path)
        cpp_file = open(args.odir + "/.vscode/c_cpp_properties.json","w")
        cpp_file.write(result)
        cpp_file.close()

        shutil.copy(ROOT_DIR + "/templates/vscode/settings.json",args.odir + "/.vscode/settings.json")

        tm = env.get_template('tasks.template')
        result = tm.render(output = args.odir + "/build/" + args.output_file, 
                           openocd_cfg = args.odir + "/spike.cfg",
                           openocd = self.openocd_path,
                           spike  = self.spike_path)
        tasks_file = open(args.odir + "/.vscode/tasks.json","w")
        tasks_file.write(result)
        tasks_file.close()

    def generateProject(self,args):
        self.createFolders(args)
        self.copyFiles(args)

        libs = str(args.libc)[2:-2].replace(".c","")
        library_str = ""
        if (args.libc):
            for n in range (len(args.libc)):
                lib_name = args.libc[n].replace(".c","")
                library_str += "add_library( " + lib_name + " STATIC " + self.output_lib_path[n] + ")" + '\n'
                library_str += "target_compile_options( " + lib_name + " PUBLIC ${COMPILER_LIST})" + '\n' 
        result = self.template.render(source = args.odir + '/' + args.source
                       , output = self.output_path
                       , libraries = library_str
                       , lib_names = libs
                       , output_dir = args.odir)
        f = open(args.odir + '/' + "CMakeLists.txt","w")
        f.write(result)
        f.close()


def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ide",type=str,help="In what IDE should the project be created",required=True, choices= {"makefile","vscode"})
    parser.add_argument("-s","--source", type=str, help="Source file to compile", required=True)
    parser.add_argument("-o","--output_file",type=str, help="Output file",required=True)
    parser.add_argument("--idir", type=str, help="Input directory",required=True)
    parser.add_argument("--odir", type=str, help="Output directory",required=True)
    parser.add_argument("--libc", type = str, help="Source library code file", required=False, nargs="+")
    parser.add_argument("--libh", type = str, help="Source library header file", required=False, nargs="+")
    return parser.parse_args()



def main():
    args = parseArguments()

    if (args.ide == "makefile"):
        project_generator = MakeProjectGenerator(args)
        project_generator.generateProject(args)

    elif (args.ide == "vscode"):
        project_generator = VSCodeGenerator(args)
        project_generator.generateProject(args)

    else: print("Not supported")


if __name__ == "__main__":
    main()




