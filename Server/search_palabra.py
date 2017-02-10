import sys
import time
from TwitsByWord import *
import os
from eliminar import *

sleep_time = 60*60

def search(busqueda, tiempo):

    ultimo = -1
    tiempo = int(tiempo)

    while(True):

        if (tiempo < 0):
            tiempo = -1

        if tiempo == 0:
            break

        ultimo = search_by_word(busqueda, ultimo)
        tiempo -= 1

        if tiempo >= 0:
            print("Busquedas restantes " + str(tiempo) + ". Pausa")
        else:
            print("Pausa")

        if(tiempo != 0):
            time.sleep(sleep_time)

    print("Fin de busquedas")
    pid = os.getpid()
    eliminarRegistro(pid)

if __name__ == '__main__':

    busqueda = sys.argv[1]
    tiempo = sys.argv[2]

    search(busqueda, tiempo)