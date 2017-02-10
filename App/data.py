#Llamar los modulos del jose
from cliente import *

class Data:
    def __init__(self):
        """La idea es guardar los process ID en una lista (como ints),
        las frases en la segunda lista como strings, mientras que
        Length lo puedes definir como el largo de las listas, notar que
        debes guardar las cosas en el mismo orden par ambas"""
        
        #info falsa para testing, setear los vectores con la info real en updateData
        self.ID = []
        self.Strings = []
        self.Length = 0
        self.updateData()

    #Lo unico que debes definir es esta funcion, yo me encargo del resto
    def updateData(self):
        #Aqui se supone que se parsean y actualizan los datos en ID y Strings
        #Te recomiendo crear una funcion que parsee la wea y te retorne una
        #lista, para luego ASIGNAR asi self.ID = funcionParse(), igual que con
        #self.Strings = funcionParse2(), ahi ingeniatelas.

        opciones = showDeleteOptions()
        self.ID = opciones[0]
        self.Strings = opciones[1]

        #Luego Length es el largo de las listas actualizadas
        self.Length = len(self.ID)
        return

    def getLength(self):
        return self.Length
