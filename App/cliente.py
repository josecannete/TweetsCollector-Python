import sys
import os
import paramiko

'''
Class ServerParameters: tiene como campos una ip (externa) del servidor, un usuario y una contraseña
'''
class ServerParameters:
    def __init__(self):
        self.ip = '35.184.125.210'
        self.username = 'lunapuljak'
        self.password = ''


'''
search: usa paramiko para conectar con el servidor y luego ejecuta una busqueda
parametrizada con client.exec_command() que interactua con el archivo querySearch del servidor
param: (string) busqueda
param: (string) currTime
param: (string) Type
param: (string) nombreArchivo
return: NULL
'''
def search(busqueda, currTime, nombreArchivo):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    directory = os.path.dirname(os.path.abspath(__file__))
    parameters = ServerParameters()
    client.connect(parameters.ip, username=parameters.username, password=parameters.password, key_filename=directory + '/llave')

    tiempo = currTime
    stdin, stdout, stderr = client.exec_command('echo | nohup python querySearch.py "' + str(tiempo) + '" "' + nombreArchivo.encode('utf-8') + '" "' + busqueda.encode('utf-8') + '" ' + '>/dev/null 2>&1 & echo $! ' + nombreArchivo.encode('utf-8') + ' >> file.txt &')
    
    client.close()

'''
delete: conecta con el servidor mediante paramiko e interactua con el archivo eliminar.py mediante client.exec_command
param: (string) pid
return: NULL
'''
def delete(pid):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    directory = os.path.dirname(os.path.abspath(__file__))
    parameters = ServerParameters()
    client.connect(parameters.ip, username=parameters.username, password=parameters.password, key_filename=directory + '/llave')


    stdin, stdout, stderr = client.exec_command('python eliminar.py ' + str(pid))
    print('Proceso ' + str(pid) + ' terminado.')

    client.close()

'''
showDeleteOptions: conecta con el servidor mediante paramiko y ejecuta en la consola del servidor "cat file.txt",
luego devuelve una lista de 2 arreglos que contienen strings de pid y texto (ordenados segun indice)
param: NULL
return: [stringList, stringList]
'''
def showDeleteOptions():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    directory = os.path.dirname(os.path.abspath(__file__))
    parameters = ServerParameters()
    client.connect(parameters.ip, username=parameters.username, password=parameters.password, key_filename=directory + '/llave')


    stdin, stdout, stderr = client.exec_command('cat file.txt')

    pidArray = []
    busquedasArray = []
    for line in stdout:
        texto = line.strip('\n').split()
        if (len(texto) >= 2):
            pid = texto[0]
            busqueda = ''
            i = 1
            while (i < len(texto)):
                busqueda += texto[i]
                busqueda += ' '
                i += 1
            pidArray.append(pid)
            busquedasArray.append(busqueda)

    client.close()

    return [pidArray, busquedasArray]
