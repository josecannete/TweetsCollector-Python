import Tkinter as tk
from Tkinter import *
import ttk
#import search_palabra as sw
#import search_person as sp
import cliente as cli

b = "Busqueda por "
t1 = "Keyword"
t2 = "Usuario"
t3 = "Eliminar Proceso"
processes = []

#Template frame to search something
class toSearch(ttk.Frame):
    def __init__(self, parent, searchType, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        
        self.toSearch = ttk.Label(self, text = searchType)
        self.toSearch.grid(row = 0, column = 0, padx = 30, pady = 10)

        self.Type = t1 if searchType == t1 else t2
        
        self.charr = ttk.Label(self, text = ("#" if searchType == t1 else "@"))
        self.charr.grid(row = 0, column = 1)

        self.Field = ttk.Entry(self, width = 34)
        self.Field.grid(row = 0, column = 2, columnspan = 2)

        self.totalTime = ttk.Label(self, text = "Tiempo Total")
        self.totalTime.grid(row = 1, column = 0, padx = 30, pady = 10)

        self.tField = ttk.Entry(self)
        self.tField.grid(row = 1, column = 2)

        self.var = tk.StringVar()
        self.tlist = ttk.Combobox(self, textvariable = self.var,
                                  values = ["Horas", "Indefinido"],
                                  state = "readonly")
        self.tlist.current(1)
        self.tlist.configure(width = 9)
        self.tlist.grid(row = 1, column = 3, padx = 5)

        self.start = ttk.Button(self,
                                text = "Comenzar",
                                command = self.searchCommand)
        self.start.grid(row = 3, column = 3)
        self.var.trace("w", self.on_trace_choice)
        self.refresh()

    #Modificar aqui thibo, ahora si que si tienes todo lo que necesitas
    def searchCommand(self):

        Type = self.Type #Puede ser "User" o "Keyword"
        String = self.Field.get() #String a buscar
        typeTime = self.tlist.get() #Puede ser "Horas" o "Indefinido"

        currTime = -1
        #Modificar estas weas, es para que veas que funciona ahora
        if typeTime == "Indefinido":
            print "El tiempo seleccionado es ", typeTime
        else:
            currTime = int(self.tField.get()) #Si no es indefinido obtenemos el int
            print "El tiempo seleccionado es ",currTime, typeTime

        print "Buscar", Type, String

        #Uso con servidor
        cli.search(String, currTime, Type)

        #Uso en consola
        """
        if Type == "Keyword":
            sw.search(String, currTime)
        if Type == "Usuario":
            sp.search(String, currTime)
        
        self.searchRefresh()
        #"""


        return
    
    #------------------Hasta aqui nomas-----------------------------------------#
    def on_trace_choice(self, name, index, mode):
        self.refresh()
        
    def refresh(self):
        typeTime = self.tlist.get()
        if typeTime == "Indefinido":
            self.tField.delete(0, "end")
            self.tField.configure(state = "disabled")
        else:
            self.tField.configure(state = "normal")
        return

    def searchRefresh(self):
        self.tlist.current(1)
        self.Field.delete(0, "end")
        return
