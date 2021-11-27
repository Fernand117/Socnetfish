# Herramienta de ingeniería social - Socnetfish

<p align="center">
 <br></br>
 <img src="https://raw.githubusercontent.com/Fernand117/Socnetfish/main/src/img/socnetfish.png">
</p>

## REQUISITOS
Para poder ejecutar y probar este script es necesario contar con una instalación de Python mayor a 3.X, es recomendable que se realice en un entorno seguro y controlado para este tipo de pruebas, el autor de este material no se hace responsable por el mal uso que se le pueda dar a esta herramienta.

Lo que necesitas instalar:
- [Python 3.X](https://www.python.org/) :snake:
- Sistema operativo Linux :penguin:



## Instalación
Una vez tengas instalada tu versión de python 3.X puedes utilizar la CL de [GIT](https://git-scm.com/) para clonar este repositorio o bien descargar directamente una copia desde el botón verde que dice "Code" en la opción "Download ZIP"

###### UTILIZANDO LA CLI DE GIT
Deberás pocicionarte en la carpeta donde desas clonar el repositorio y estando allí ejecutar el comando:
```
git clone https://github.com/Fernand117/Socnetfish.git
```

###### INSTALANDO EL PROGRAMA
Para instalar Socnetfish en tu computadora entra a la carpeta del proyecto que acabas de clonar y ejecuta

```
sudo python3 setup.py
```
Esto iniciará la instalación de paquetes necesarios para que la aplicación pueda funcionar correctamente.

Para desinstalar Socnetfish de tu equipo, basta con ejecutar el programa que viene en la misma carpeta que se ha clonado del
repositorio de git, con el siguiente comando

```
python3 uninstall.py
```
Este comando desinstalará el programa de tu equipo.

###### EJECUCIÓN

Una vez instalado el programa, podras ejecutar desde tu terminal el siguiente comando:
```
socnetfish
```
## ¿CÓMO FUNCIONA?
Una vez ejecutado el script este comenzará a verificar que exista ngrok, en caso de que no, lo descagará automáticamente desde la web oficial.

Una vez hecho esto el script ejecutará en un servidor local el sitio que se pretende clonar.

Cuando el sitio detecte una contraseña, esta se listará en la terminal.

Para terminar la ejecución del script habrá dos opciones, la primera es que antes de iniciar el servidor tendrás una opción en el menú principal que te permitirá terminarla y la segunda es que estando el servidor activo preciones la combinación de teclas Ctrl+c en tu teclado y este preguntará si deseas terminar la ejecución.

## NOTA IMPORTANTE
Deberá ejectuar en otra terminal el siguiente comando para que el servidor local quede expuesto a internet y entonces poder utilizarse desde cualquier dispositivo fuera de la red.

```
./ngrok http 8080
```



## GRACIAS
##### El autor de este material no se hace responsable por el mal uso que se le pueda dar. El contenido de este repositorio es con fines de aprendizaje.

Creado por Luis Fernando Leyva Luna

Sígueme en Instagram: <img src="https://www.instagram.com/static/images/ico/apple-touch-icon-76x76-precomposed.png/666282be8229.png" style="width:25px"> [@fernand_117](https://www.instagram.com/fernand_117/?hl=es-la)
