import sys
import os
import paramiko



def search(busqueda, currTime, Type, nombreArchivo):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    directory = os.path.dirname(os.path.abspath(__file__))
    client.connect('35.184.125.210', username='lunapuljak', password='', key_filename=directory + '/llave')

    tipo = Type

    # tipo sera una de estas opciones: [search, name, delete]

    if tipo == 'Keyword' or tipo == 'Usuario':
        tiempo = currTime
        if tipo == 'Keyword':
            stdin, stdout, stderr = client.exec_command('echo | nohup python querySearch.py "' + str(tiempo) + '" "' 
                + nombreArchivo.encode('utf-8') + '" "' + busqueda.encode('utf-8') + '" ' + '>/dev/null 2>&1 & echo $! ' + nombreArchivo.encode('utf-8') + ' >> file.txt &')
        else:
            stdin, stdout, stderr = client.exec_command('echo | nohup python querySearch.py "' + str(tiempo) + '" "'
             + nombreArchivo.encode('utf-8') + '" ' + busqueda.encode('utf-8') + ' ' + '>/dev/null 2>&1 & echo $! ' + nombreArchivo.encode('utf-8') + ' >> file.txt &')
    else:
        print('Opcion no valida')
    client.close()


# borrar instancias existentes

def delete(pid):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    directory = os.path.dirname(os.path.abspath(__file__))
    client.connect('35.184.125.210', username='lunapuljak', password='', key_filename=directory + '/llave')

    stdin, stdout, stderr = client.exec_command('python eliminar.py ' + str(pid))
    print('Proceso ' + str(pid) + ' terminado.')

    client.close()

def showDeleteOptions():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    directory = os.path.dirname(os.path.abspath(__file__))
    client.connect('35.184.125.210', username='lunapuljak', password='', key_filename=directory + '/llave')

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
