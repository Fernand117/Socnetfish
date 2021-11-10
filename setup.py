#!/usr/bin/python3

import os
import subprocess

from getpass import getuser

print("[*] Instalando requerimientos...")
subprocess.Popen("python3 -m pip install requirements.txt", shell=True).wait()

print("[*] Instalando socnetfish en /usr/share/socnetfish..")
print(os.getcwd())
subprocess.Popen("mkdir /usr/share/socnetfish/; cp -r src/ /usr/share/socnetfish/", shell=True).wait();

print("[*] Creando lanzador de socnetfish...")
filewrite = open("/usr/local/bin/socnetfish", "w")
filewrite.write("#!/bin/sh\ncd /usr/share/socnetfish/src\n./socnetfish")
filewrite.close()

print("[*] Listo, Modificando permisos de ejecución +x...")
subprocess.Popen("chmod +x /usr/local/bin/socnetfish", shell=True).wait()

print("[*] Instalación finalizada. Ejecute socnetfish para iniciar.")
