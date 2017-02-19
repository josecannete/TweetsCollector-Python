import sys
import os
import time
from eliminar import *

def search(query, tiempo, nombreArchivo):

  tiempo = int(tiempo)
    
  while (True):
    fecha = time.strftime("%d.%m.%Y")

    if (tiempo == 0):
        break

    dir_path = os.path.dirname(os.path.realpath(__file__))
    #print("twarc search '" + query + "' > " + dir_path + "/busquedas/" + nombreArchivo + fecha + ".json")
    os.system("twarc search '" + query + "' > " + dir_path + "/busquedas/" + nombreArchivo + fecha + ".json")

    tiempo -= 1

    if (tiempo != 0):
      time.sleep(7 * 24 * 60 * 60)

if __name__ == '__main__':

    tiempo = sys.argv[1]
    nombreArchivo = sys.argv[2]
    busqueda = sys.argv[3]

    search(busqueda, tiempo, nombreArchivo)
    pid = os.getpid()
    eliminarRegistro(pid)