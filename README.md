# Socnetfish

<p align="center">
 <br></br>
 <img src="https://www.python.org/static/img/python-logo.png">
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

###### INSTALANDO LIBRERÍAS ADICIONALES
Para correr este script es necesaria la instalación de las siguientes librerías

Colorama
```
python3 -m pip install colorama
```

Zipfile

```
python3 -m pip install zipfile
```



###### EJECUCIÓN

Una vez clonado el repositorio entrar desde tu terminal Linux y dentro de la carpeta src ejecutar:
```
python3 socnetfish.py
```
## ¿CÓMO FUNCIONA?
Una vez ejecutado el script este comenzará a verificar que exista ngrok, en caso de que no, lo descagará automáticamente desde la web oficial.

Una vez hecho esto el script ejecutará en un servidor local el sitio que se pretende clonar.

Cuando el sitio detecte una contraseña, esta se listará en la terminal.

Para terminar la ejecución del script habrá dos opciones, la primera es que antes de iniciar el servidor tendrás una opción en el menú principal que te permitirá terminarla y la segunda es que estando el servidor activo preciones la combinación de teclas Ctrl+c en tu teclado y este preguntará si deseas terminar la ejecución.

## NOTA IMPORTANTE
Deberá ejectuar en el mismo lugar en otra terminal el siguiente comando para que el servidor local quede expuesto a internet y entonces poder utilizarse desde cualquier dispositivo fuera de la red.

```
./ngrok http 8080
```



## GRACIAS
##### El autor de este material no se hace responsable por el mal uso que se le pueda dar. El contenido de este repositorio es con fines de aprendizaje.

Creado por Luis Fernando Leyva Luna
Sígueme en Instagram: [@fernand_117](https://www.instagram.com/fernand_117/?hl=es-la)

