import Tkinter as tk
from Tkinter import *
import ttk
from tkSearch import *
from tkDelete import *

b = "Busqueda"
t1 = "Keyword"
t2 = "Usuario"
t3 = "Procesos"
processes = []

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
        titles = [b, t3]
        self.frames = {}
        for title in titles:
            self.frames[title] = ttk.Frame(self.tab)
            self.tab.add(self.frames[title], text = title)

        #Frame for search
        self.searchKey = toSearch(self.frames[b], b, self)
        self.searchKey.pack()

        #Frame for list of processes
        self.deleteList = toDelete(self.frames[t3], self)
        self.deleteList.pack()
        
        self.tab.pack()
        

app = TwitterApp()
app.title("Twitter App")
app.geometry('565x330')
app.mainloop()
        
