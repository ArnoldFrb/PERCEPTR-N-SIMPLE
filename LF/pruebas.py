import numpy as np
import random as rn 
import pandas as pd
from tkinter import filedialog
from tkinter import *

class pruebas:
    def __init__(self,data = 'LF/Data/prueba.csv',encabezado = 0):
        self.dataSet = pd.read_csv(data,header=encabezado)

    def GetEntradas(self,index = []):
        
        matriz = self.dataSet.to_numpy()
        return matriz

    def GetSalidas(self,index = []):
        matriz = self.dataSet.to_numpy()
        return matriz

class View:
    def __init__(self):

        def selectEntrada():
            self.fileEntrada = filedialog.askopenfilename()

        self.root = Tk()
        self.root.title('Perceptron Simple')

        self.root.geometry('400x400')

        frame_input_output = Frame(self.root)
        frame_input_output.place(relx=.01,rely=.01,relwidth=.33,relheight=.11)

        btnSelectEntradas = Button(self.root, text="Cargar entrada", command=lambda:selectEntrada())
        btnSelectEntradas.place(relx=.05,rely=.01,relwidth=.25,relheight=.30)

        self.root.mainloop()


p = pruebas()
v = View()

