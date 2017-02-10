import sys
import os
import paramiko



def search(busqueda, currTime, Type):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    directory = os.path.dirname(os.path.abspath(__file__))
    client.connect('104.197.72.131', username='lunapuljak', password='', key_filename=directory + '/llave')

    tipo = Type

    # tipo sera una de estas opciones: [search, name, delete]

    if tipo == 'Keyword' or tipo == 'Usuario':
        tiempo = currTime
        if tipo == 'Keyword':
            stdin, stdout, stderr = client.exec_command('nohup python search_palabra.py ' + str(busqueda) + ' ' + str(tiempo) + ' ' +
                                                        '>/dev/null 2>&1 & echo $! &')
        else:
            stdin, stdout, stderr = client.exec_command('nohup python search_person.py ' + str(busqueda) + ' ' + str(tiempo) + ' ' +
                                                        '>/dev/null 2>&1 & echo $! &')
        pid = ''
        for line in stdout:
            pid = line.strip('\n')
        linea = 'echo ' + str(pid) + ' ' + str(busqueda) + ' >> file.txt'
        stdin, stdout, stderr = client.exec_command(linea)
    else:
        print('Opcion no valida')
    client.close()


# borrar instancias existentes

def delete(pid):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    directory = os.path.dirname(os.path.abspath(__file__))
    client.connect('104.197.72.131', username='lunapuljak', password='', key_filename=directory + '/llave')

    stdin, stdout, stderr = client.exec_command('python eliminar.py ' + str(pid))
    print('Proceso ' + str(pid) + ' terminado.')

    client.close()

def showDeleteOptions():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    directory = os.path.dirname(os.path.abspath(__file__))
    client.connect('104.197.72.131', username='lunapuljak', password='', key_filename=directory + '/llave')

    stdin, stdout, stderr = client.exec_command('cat file.txt')

    pidArray = []
    busquedasArray = []
    for line in stdout:
        texto = line.strip('\n').split()
        pid = texto[0]
        busqueda = texto[1]
        pidArray.append(pid)
        busquedasArray.append(busqueda)

    client.close()

    return [pidArray, busquedasArray]