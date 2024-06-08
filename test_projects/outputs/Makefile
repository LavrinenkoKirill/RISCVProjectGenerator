build-make:
	make -C make/

build-vscode:
	cd vscode/build/ && cmake ../ && make

build-eclipse:
	cd eclipse-workspace && /home/lavrinenko/eclipse_embedded/eclipse/eclipse --launcher.suppressErrors -nosplash -application org.eclipse.cdt.managedbuilder.core.headlessbuild -data . -import eclipse-project/ -build all
	
