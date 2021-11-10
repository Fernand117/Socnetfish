#!/usr/bin/python3

import os
import subprocess

from getpass import getuser

print("[*] Desinstalando socnetfish de /usr/share/socnetfish..")
print(os.getcwd())
subprocess.Popen("sudo rm -r /usr/share/socnetfish/", shell=True).wait();

print("[*] Eliminando lanzador de socnetfish...")
subprocess.Popen("sudo rm -r /usr/local/bin/socnetfish", shell=True).wait()

print("[*] Eliminando archivos de configuración...")
subprocess.Popen("rm -r /home/" + getuser() + "/.config/socnetfish", shell=True).wait()

print("[*] Desinstalación finalizada.")
