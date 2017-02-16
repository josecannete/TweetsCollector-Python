#Llamar los modulos del jose
from cliente import *

class Data:
    def __init__(self):
        self.ID = []
        self.Strings = []
        self.Length = 0
        self.updateData()

    def updateData(self):
        opciones = showDeleteOptions()
        self.ID = opciones[0]
        self.Strings = opciones[1]
        self.Length = len(self.ID)
        return

    def getLength(self):
        return self.Length
