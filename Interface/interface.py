import Tkinter as tk
from Tkinter import *
import ttk
from tkSearch import *
from tkDelete import *

b = "Busqueda por "
t1 = "Keyword"
t2 = "Usuario"
t3 = "Eliminar Proceso"
processes = []
jajaja = 0

#Main window
class TwitterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #Title inside window on top
        self.topLabel = tk.Label(self, text = "Twitter App")
        self.topLabel.pack()

        #Tab interface
        self.tab = ttk.Notebook(self)

        #Adding titles to tabs
        titles = [b + t1, b + t2, t3]
        self.frames = {}
        for title in titles:
            self.frames[title] = ttk.Frame(self.tab)
            self.tab.add(self.frames[title], text = title)

        #Frame for search tweets by key
        self.searchKey = toSearch(self.frames[b+t1], t1, self)
        self.searchKey.pack()

        #Frame for search tweets by user
        self.searchUsr = toSearch(self.frames[b+t2], t2, self)
        self.searchUsr.pack()

        #Frame for list of processes
        self.deleteList = toDelete(self.frames[t3], self)
        self.deleteList.pack()
        
        self.tab.pack()
        

app = TwitterApp()
app.title("Twitter App")
app.geometry('500x380')
app.mainloop()
        
