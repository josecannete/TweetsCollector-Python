import sys
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('104.197.245.208', username='joserodolfocl', password='', key_filename='/Users/Jose/Desktop/llave')

tipo = sys.argv[1]

# tipo sera una de estas opciones: [search, name, delete]

if tipo == 'search' or tipo == 'name':
    busqueda = raw_input('Ingrese texto a buscar: ')
    tiempo = raw_input('Ingrese tiempo total de ejecucion: ')
    if tipo == 'search':
        stdin, stdout, stderr = client.exec_command('nohup python dummySearch.py ' + busqueda + ' ' + tiempo + ' ' +
                                                    '>/dev/null 2>&1 & echo $! &')
    else:
        stdin, stdout, stderr = client.exec_command('nohup python dummyName.py ' + busqueda + ' ' + tiempo + ' ' +
                                                    '>/dev/null 2>&1 & echo $! &')
    pid = ''
    for line in stdout:
        pid = line.strip('\n')
    linea = 'echo ' + pid + ' Busqueda: ' + busqueda + ' >> file.txt'
    stdin, stdout, stderr = client.exec_command(linea)


# borrar instancias existentes
elif tipo == 'delete':
    stdin, stdout, stderr = client.exec_command('cat file.txt')
    numero = 0
    pidArray = []
    for line in stdout:
        numero += 1
        print(numero)
        pid = line.strip('\n')
        pidArray += pid
        print(' ' + pid)
    opcionEliminar = raw_input()
    if opcionEliminar < 0 or opcionEliminar > numero:
        print("Opcion invalida, escriba una correcta")
        opcionEliminar = raw_input()
    else:
        stdin, stdout, stderr = client.exec_command('python eliminar.py ' + pidArray[opcionEliminar - 1])
        print('Proceso ' + opcionEliminar + ' terminado.')


else:
    print('Opcion no valida')


client.close()
