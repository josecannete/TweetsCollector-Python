# TweetsCollector-Python

# Instrucciones para el setup del servidor

1 - Descargar los archivos de la carpeta Server y copiarlos dentro de la carpeta Home del servidor.

2 - Instalar y configurar twarc (https://github.com/DocNow/twarc).

3 - Dentro de la carpeta home crear un directorio llamado "busquedas" en el que se almacenaran los .json (Recordar que twarc guarda line-oriented JSON).

# Instrucciones para el setup del cliente

1 - Instalar paramiko (http://www.paramiko.org/installing.html) y tkinter (en caso de no estar instalado, http://www.paramiko.org/installing.html)

2 - Descargar la carpeta App.

3 - Modificar el archivo cliente.py (https://github.com/josecannete/TweetsCollector-Python/blob/master/App/cliente.py) con los datos de su servidor.

4 - Reemplazar el archivo "llave" que está en la carpeta App por el adecuado para su servidor (esto es una llave de conección SSH).

# Instrucciones de uso del cliente

1 - Desde el terminal entrar a la carpeta App y ejecutar el archivo interface.py como se muestra a continuación:

![alt tag](http://i.imgur.com/i0QcXcZ.png)

2 - Se abrirá una ventana como la que se muestra a continuación:

![alt tag](http://i.imgur.com/KG5XRhj.png)

3 - Para ejecutar una busqueda debemos completar los campos que se indican. En el campo Busqueda debemos ingresar la consulta deseada, la sintaxis de esta es la misma de twarc y de la busqueda avanzada de Twitter (https://twitter.com/search-advanced?lang=es). Un ejemplo rápido es la siguiente busqueda (https://twitter.com/search?l=&q=hola%20OR%20mundo&src=typd&lang=es):

![alt tag](http://i.imgur.com/iizToU7.png)

Donde la consulta que nos interesa es la siguiente, este texto es el que debemos ingresar en el parametro de busqueda:

![alt tag](http://i.imgur.com/xxS2pse.png)
![alt tag](http://i.imgur.com/tDAAxdv.png)


Por otra parte, el tiempo a ejecutar se ingresa en Semanas o de manera indefinida. En el primer caso lo que haremos será buscar cada semana los tweets de los ultimos 7 dias (esto también puede ajustarse para menos días modificando correctamente la consulta). Es decir, si decidimos, por ejemplo, poner 3 semanas como parametro, obtendremos los tweets de la semana anterior y las 2 siguientes al día en que se ejecuta la consulta. En el segundo caso, se ejecutará una busqueda semanal hasta que detengamos el proceso de manera posterior.

Finalmente, debemos ingresar un parametro de nombre de archivo, y es simplemente el nombre del archivo que contendrá los tweets a archivar. El formato del nombre, en el servidor, quedará de la siguiente manera: nombre_de_archivo + dia.fecha.año + extensión JSON. En el caso de la busqueda anterior, nuestra primera busqueda quedaría como tweetsdeholachao10.10.2017.json. Notemos que cada semana se guardará un archivo distinto con la fecha de los tweets de esa semana.

Una consulta quedaría finalmente así:

![alt tag](http://i.imgur.com/82iKWhy.png)

4 - Existe una segunda pestaña, llamada Pestaña de Procesos. La función de esta es el permitirnos detener busquedas que estén corriendo en el servidor. Una vez abierta nos mostrará una lista con los procesos corriendo en el servidor:

![alt tag](http://i.imgur.com/MjqFVdw.png)

Luego, para detener uno o varios procesos solo tendremos que seleccionarlos y posteriormente dar click en el botón Terminar:

![alt tag](http://i.imgur.com/ItiLKpc.png)

5 - Una vez que hayamos hecho una busqueda o eliminado un proceso, los campos de información se actualizaran y podremos seguir ejecutando acciones, o bien cerrar el programa.
