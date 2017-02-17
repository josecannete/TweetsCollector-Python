import sys
import os

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

def eliminarProceso(pid):
    os.system('kill ' + str(pid))
    return 0

if __name__ == '__main__':
    pid = sys.argv[1]
    eliminarRegistro(pid)
    eliminarProceso(pid)

