# TweetsCollector-Python

# Instrucciones para el setup del servidor

1 - Descargar los archivos de la carpeta Server y copiarlos dentro de la carpeta Home del servidor.

2 - Instalar y configurar twarc (https://github.com/DocNow/twarc).

3 - Dentro de la carpeta home crear un directorio llamado "busquedas" en el que se almacenaran los .json (Recordar que twarc guarda line-oriented JSON).

# Instrucciones para el setup del cliente

1 - Instalar paramiko (http://www.paramiko.org/installing.html) y tkinter (en caso de no estar instalado, http://www.paramiko.org/installing.html)

2 - Descargar la carpeta App.

3 - Modificar el archivo cliente.py (https://github.com/josecannete/TweetsCollector-Python/blob/master/App/cliente.py) con los datos de su servidor.

4 - Reemplazar el archivo "llave" que está en la carpeta App por el adecuado para su servidor (esto es una llave de conneción SSH).

