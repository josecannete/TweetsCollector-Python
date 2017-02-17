import sys
import time
from SomeoneTweets import *
import os
from eliminar import *

sleep_time = 20*60

def search(busqueda, tiempo):

    ultimo = -1
    tiempo = int(tiempo)

    while(True):

        if(tiempo < 0):
            tiempo = -1

        if tiempo == 0:
            break
            
        tiempo -= 1

        if tiempo >= 0:
            print ("Busquedas restantes "+str(tiempo)+". Pausa")
        else :
            print ("Pausa")
            
        for j in range(3):
            
            ultimo = search_by_user(busqueda, ultimo)
            
            if(not (tiempo == 0 and j == 2) ):
                time.sleep(sleep_time)

    print ("Fin de busquedas")
    pid = os.getpid()
    eliminarRegistro(pid)

if __name__ == '__main__':

    busqueda = sys.argv[1]
    tiempo = sys.argv[2]
    # para evitar problemas de sincronizacion
    time.sleep(60)
    search(busqueda, tiempo)

