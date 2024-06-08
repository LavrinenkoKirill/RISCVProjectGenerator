import os
from jinja2 import Environment,FileSystemLoader,Template
import argparse
import shutil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class ProjectGenerator:
    def __init__(self,args):
        self.libc = args.libc
        self.libh = args.libh
        self.odir = args.odir
        self.idir = args.idir
        self.bsp_dir = args.odir + "/bsp"
        self.openocd_file = args.odir + "/spike.cfg"
        self.build_dir = args.odir + "/build"
        self.executable_path = "build/" + args.output_file
        self.source = args.source
        self.output_file = args.output_file
        if (args.cflags):
            for i in range (len(args.cflags)):
                args.cflags[i] = "-" + args.cflags[i]
            delimiter = " "
            self.cflags = delimiter.join(args.cflags)
        else: self.cflags = ""

        self.source_path = args.idir + '/' + args.source
        if (args.libc):
            self.obj_lib_path = [None] * len(args.libc) 
            for n in range(len(args.libc)):
                self.obj_lib_path[n] = "object/" + args.libc[n].replace(".c",".o")
        else: self.obj_lib_path = ""
        if (args.libh):
            self.header_lib_path = [None] * len(args.libh)
            for (n) in range(len(args.libh)): 
                self.header_lib_path[n] = args.idir + '/' + args.libh[n]
        else: self.header_lib_path = ""

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
        

    
    def createFolders(self):
        if (os.path.isdir(self.build_dir) == False): os.mkdir(self.build_dir)
            

    def copyFiles(self):
        if (self.libh):
            for (n) in range(len(self.libh)): 
                if (self.idir != self.odir): shutil.copy(self.header_lib_path[n],self.odir + '/' + self.libh[n])
        
        if (self.idir != self.odir): shutil.copy(self.source_path,self.odir + '/' + self.source)
        if (os.path.isdir(self.bsp_dir) == False):shutil.copytree(ROOT_DIR + "/bsp",self.bsp_dir)
        if (os.path.isfile(self.openocd_file) == False):shutil.copy(ROOT_DIR + "/templates/spike.cfg",self.openocd_file)
            

        if (self.libc):
            for i in range (len(self.libc)):
                if (self.idir != self.odir): shutil.copy(self.idir + '/' + self.libc[i],self.odir + '/' + self.libc[i])

class MakeProjectGenerator(ProjectGenerator):
    def __init__(self,args):
        super().__init__(args)
        file_loader = FileSystemLoader(ROOT_DIR + '/templates')
        env = Environment(loader = file_loader)
        self.template = env.get_template('Makefile.template')
        self.object_dir = args.odir + "/object"
        self.obj_main_path = "object/" + args.source.replace(".c",".o")

    def createFolders(self):
        super().createFolders()
        if (os.path.isdir(self.object_dir) == False): os.mkdir(self.object_dir)

    def createDebugScripts(self):
        bash_templates_loader = FileSystemLoader(ROOT_DIR + '/templates/bash')
        env = Environment(loader = bash_templates_loader)
        tm = env.get_template('start_debug.template')
        result = tm.render(executable = self.executable_path, 
                           spike_path = self.spike_path,
                           openocd_path = self.openocd_path,
                           gdb_path = self.gdb_path)
        f = open(self.odir + "/start_debug.sh","w")
        f.write(result)
        shutil.copy(ROOT_DIR + "/templates/bash/end_debug.sh",self.odir + "/end_debug.sh")
        shutil.copy(ROOT_DIR + "/templates/bash/commands.txt",self.odir + "/commands.txt")

    def generateProject(self):
        self.createFolders()
        super().copyFiles()
        delimiter = " "
        object_str = delimiter.join(self.obj_lib_path)
        header_str = delimiter.join(self.libh)
        
    
        result = self.template.render(source = self.source
                       , compiler_path = self.compiler_path
                       , output = self.executable_path
                       , main_obj = self.obj_main_path
                       , lib_obj = object_str
                       , lib_h = header_str
                       , cflags = self.cflags)

        f = open(self.odir + "/Makefile","w")
        f.write(result)

        if (self.libc):
            for n in range (len(self.libc)):
                obj_string = self.obj_lib_path[n] + ' : ' + self.libc[n] + " " + self.libh[n]
                f.write(obj_string)
                f.write('\n')
                f.write('\t' + "$(GCC) -o " + self.obj_lib_path[n] + " -c " + self.libc[n] + " $(COMPILER_FLAGS)")
                f.write('\n')
        f.close()

        self.createDebugScripts()


class VSCodeGenerator(ProjectGenerator):
    def __init__(self,args):
        super().__init__(args)
        file_loader = FileSystemLoader(ROOT_DIR + '/templates')
        env = Environment(loader = file_loader)
        self.template = env.get_template('CMakeLists.template')
        self.vsfolder = args.odir + "/.vscode"
    
    def createFolders(self):
        super().createFolders()
        if (os.path.isdir(self.vsfolder) == False): os.mkdir(self.vsfolder)

    def generateProject(self):
        self.createFolders()
        super().copyFiles()

        vs_templates_loader = FileSystemLoader(ROOT_DIR + '/templates/vscode')
        env = Environment(loader = vs_templates_loader)
        tm = env.get_template('launch.template')
        result = tm.render(output = self.executable_path,
                           gdb = self.gdb_path)
        launch_file = open(self.vsfolder + "/launch.json","w")
        launch_file.write(result)
        launch_file.close()

        tm = env.get_template("c_cpp_properties.template")
        result = tm.render(compiler = self.compiler_path)
        cpp_file = open(self.vsfolder + "/c_cpp_properties.json","w")
        cpp_file.write(result)
        cpp_file.close()

        shutil.copy(ROOT_DIR + "/templates/vscode/settings.json",self.vsfolder + "/settings.json")

        tm = env.get_template('tasks.template')
        result = tm.render(output = self.executable_path, 
                           openocd = self.openocd_path,
                           spike  = self.spike_path)
        tasks_file = open(self.vsfolder + "/tasks.json","w")
        tasks_file.write(result)
        tasks_file.close()
        
        delimiter = " "
        libs = delimiter.join(self.libc)
        libs = libs.replace(".c","")

        library_str = ""
        if (self.libc):
            for n in range (len(self.libc)):
                lib_name = self.libc[n].replace(".c","")
                library_str += "add_library( " + lib_name + " STATIC " + self.libc[n] + ")" + '\n'
                library_str += "target_compile_options( " + lib_name + " PUBLIC ${COMPILER_LIST})" + '\n' 
        result = self.template.render(source = self.source
                       , output = self.output_file
                       , libraries = library_str
                       , lib_names = libs
                       , compiler = self.compiler_path
                       , cflags = self.cflags)
        f = open(self.odir + '/' + "CMakeLists.txt","w")
        f.write(result)
        f.close()


class EclipseProjectGenerator(ProjectGenerator):
    def __init__(self,args):
        super().__init__(args)
        self.bsp_dir = args.odir + "/src/bsp"
        self.build_dir = args.odir + "/src"

        if (args.libc):
            self.output_lib_path = [None] * len(args.libc)
            for (n) in range(len(args.libc)): 
                self.output_lib_path[n] = args.odir + '/' + args.libc[n]
        else: self.output_lib_path = ""
    
    def copyFiles(self):
        if (self.libh):
            for (n) in range(len(self.libh)): 
                shutil.copy(self.header_lib_path[n],self.build_dir + '/' + self.libh[n])
        
        shutil.copy(self.source_path,self.build_dir + '/' + self.source)
        if (os.path.isdir(self.bsp_dir) == False):shutil.copytree(ROOT_DIR + "/bsp",self.bsp_dir)
        if (os.path.isfile(self.openocd_file) == False):shutil.copy(ROOT_DIR + "/templates/spike.cfg",self.openocd_file)

        if (self.libc):
            for i in range (len(self.libc)):
                shutil.copy(self.idir + '/' + self.libc[i],self.build_dir + '/' + self.libc[i])


    
    def generateProject(self):
        super().createFolders()
        self.copyFiles()

        eclipse_templates_loader = FileSystemLoader(ROOT_DIR + '/templates/eclipse')
        env = Environment(loader = eclipse_templates_loader)
        project_template = env.get_template('project.template')
        project_path = self.odir.split('/')
        project_name = project_path[-1]
        result = project_template.render(project = project_name)
        project_file = open(self.odir + "/.project","w")
        project_file.write(result)
        project_file.close()

        cproject_template = env.get_template('cproject.template')
        result = cproject_template.render(project = project_name,
                                          output_dir = self.odir,
                                          cflags = self.cflags)
        cproject_file = open(self.odir + "/.cproject","w")
        cproject_file.write(result)
        cproject_file.close()


        tm = env.get_template('Debug.template')
        project_path = self.odir.split('/')
        project_name = project_path[-1]
        result = tm.render(openocd_path = self.openocd_path,
                           gdb_path = self.gdb_path,
                           output = project_name + ".elf",
                           output_dir = project_name)
        debug_file = open(self.odir + "/Debug.launch","w")
        debug_file.write(result)
        debug_file.close()

        bash_templates_loader = FileSystemLoader(ROOT_DIR + '/templates/bash')
        bash_env = Environment(loader = bash_templates_loader)
        tm = bash_env.get_template('start_spike.template')
        result = tm.render(spike_path = self.spike_path,
                           executable = project_name + ".elf")
        spike_file = open(self.odir + "/start_spike.sh","w")
        spike_file.write(result)
        spike_file.close()



def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ide",type=str,help="In what IDE should the project be created",required=True, choices= {"makefile","vscode","eclipse"})
    parser.add_argument("--idir", type=str, help="Input directory",required=True)
    parser.add_argument("-s","--source", type=str, help="Source file to compile", required=True)
    parser.add_argument("--libc", type = str, help="Additional files for build", required=False, nargs="+")
    parser.add_argument("--libh", type = str, help="Headers for build", required=False, nargs="+")
    parser.add_argument("--odir", type=str, help="Output directory",required=True)
    parser.add_argument("-o","--output_file",type=str, help="Output file",required=True)
    parser.add_argument("--cflags", type = str, help = "Flags for compilation", required=False, nargs="+")
    parser.add_argument("--ldflags", type = str, help = "Flags for linking", required=False, nargs = "+")
    return parser.parse_args()



def main():
    args = parseArguments()

    if (args.ide == "makefile"):
        project_generator = MakeProjectGenerator(args)
        project_generator.generateProject()

    elif (args.ide == "vscode"):
        project_generator = VSCodeGenerator(args)
        project_generator.generateProject()
    
    elif (args.ide == "eclipse"):
        project_generator = EclipseProjectGenerator(args)
        project_generator.generateProject()

    else: print("Not supported")


if __name__ == "__main__":
    main()




