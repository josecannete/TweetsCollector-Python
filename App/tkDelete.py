import Tkinter as tk
from Tkinter import *
import ttk
import cliente
from data import *

b = "Busqueda por "
t1 = "Keyword"
t2 = "Usuario"
t3 = "Eliminar Proceso"
processes = []

#Template Frame to Delete Processes
class toDelete(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Data object
        self.data = Data()

        #Top Frame with raised labels
        self.topFrame = tk.Frame(self)
        self.number = tk.Label(self.topFrame, relief = RAISED,
                               text = " Numero ",
                               anchor = W).grid(row = 0, column = 0)
        self.id = tk.Label(self.topFrame, relief = RAISED,
                           text = 3*" "+"ID"+5*" ").grid(row = 0, column = 2)
        self.text = tk.Label(self.topFrame, relief = RAISED,
                             text = 6*" "+"Texto"+30*" ").grid(row = 0, column = 3)
        self.topFrame.grid(row = 0, column = 0, sticky = W)

        #Center Frame which contain the list
        self.cframe = tk.Frame(self)
        self.canvas = tk.Canvas(self.cframe, background="#ffffff", width = 300)
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self.cframe, orient="vertical",
                                jump = 0, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
    
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", expand = YES)
        self.canvas.create_window((0,0), window=self.frame, tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        
        self.textCheckButton(self.data.getLength())
        self.cframe.grid(row = 1, column = 0, rowspan = 12, columnspan = 5)

        #End Process Button
        self.end = ttk.Button(self, text = "Terminar", command = self.endCommand)
        self.end.grid(row = 13, column = 1)

        
    #Elements from the lists imported as lists
    def textCheckButton(self, n):
        self.bList = [tk.IntVar() for i in range(self.data.getLength())]
        for i in range(n):
            tk.Label(self.frame, text= str(i), width = 3, borderwidth = 0,
                     relief = "solid", anchor = W,
                     background = "#ffffff").grid(row = i, column=0)

            tk.Label(self.frame, text= str(self.data.ID[i]),
                background="#ffffff",
                anchor = W).grid(row = i, column = 1, padx = 30)

            tk.Label(self.frame,
                     text = self.data.Strings[i],
                     background="#ffffff",
                     width = 21,
                     anchor = W).grid(row = i, column=2)

            tk.cb = tk.Checkbutton(self.frame, variable = self.bList[i],
                                   background="#ffffff",).grid(row = i,
                                                               column = 3)
    #Reset the scroll region to encompass the inner frame
    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    #Aqui deben modificar!!!------------------------------------------------#
    def endCommand(self):
        for i in range(self.data.getLength()):
            if self.bList[i].get() == 1:
                processID = self.data.ID[i]
                cliente.delete(processID)
                print "proceso", processID, "seleccionado, por eliminar\n"
       
        self.updateWindow()
        
    def updateWindow(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
            
        self.data.updateData()
        self.textCheckButton(self.data.getLength())
        self.cframe.grid(row = 1, column = 0, rowspan = 12, columnspan = 5)

                
