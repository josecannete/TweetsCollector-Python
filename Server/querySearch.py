import sys
import os
import time

def search(query, tiempo):

  tiempo = int(tiempo)
    
  while (True):
    fecha = time.strftime("%d.%m.%Y")

    if (tiempo == 0):
        break

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("twarc search '" + query + "' > " + dir_path + "/busquedas/" + 
        query + fecha + ".json")
    os.system("twarc search '" + query + "' > " + dir_path + "/busquedas/busqueda" + fecha + ".json")

    tiempo -= 1

    if (tiempo != 0):
      time.sleep(7 * 24 * 60 * 60)

if __name__ == '__main__':
    
    busqueda = ''
    i = 1
    while (i < len(sys.argv) - 1):
        busqueda += sys.argv[i]
        i += 1
        if (i < len(sys.argv) - 1):
            busqueda += ' '
    tiempo = sys.argv[len(sys.argv) - 1]
    # para evitar problemas de sincronizacion
    #time.sleep(60)
    search(busqueda, tiempo)