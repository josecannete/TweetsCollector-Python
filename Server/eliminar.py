import sys
import os

'''
eliminarRegistro: busca en el archivo file.txt la linea que inicia con el string PID y la elimina
param: (string) pid
return: NULL
'''
def eliminarRegistro(pid):
    archivo = open("file.txt", "r")
    lines = archivo.readlines()
    archivo.close()

    archivo = open("file.txt", "w")
    for line in lines:
        print(line)
        if not line.startswith(str(pid)):
            archivo.write(line)
    archivo.close()
    return 0

'''
eliminarProceso: elimina un proceso corriendo (mediante os.system y el comando kill)
param: (string) pid
return: NULL
'''
def eliminarProceso(pid):
    os.system('kill ' + str(pid))
    return 0

'''
main: ejecuta eliminarRegistro y posteriormente eliminarProceso
param: (string) pid
return: NULL
ejemplo: python eliminar.py 1230
'''
if __name__ == '__main__':
    pid = sys.argv[1]
    eliminarRegistro(pid)
    eliminarProceso(pid)

