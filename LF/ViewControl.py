from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from Neurona import *

class ViewControl:

    def loadData(self,entry):
        fileEntrada = filedialog.askopenfilename()
        entry.insert(0, fileEntrada)
        return fileEntrada
    
    def llenarTabla(self,treeview,dataframe):
        treeview.delete(*treeview.get_children())
        treeview["column"] = list(dataframe.columns)
        treeview["show"] = "headings"

        for column in treeview["columns"]:
            treeview.heading(column, text=column)

        df_rows = dataframe.to_numpy().tolist()
        for row in df_rows:
            treeview.insert("", "end", values=row)

    def crearGrid(self,treeview,frame):
        treeview.place(relheight=1, relwidth=1)
        treescrolly = Scrollbar(frame, orient="vertical", command=treeview.yview)
        treescrollx = Scrollbar(frame, orient="horizontal", command=treeview.xview)
        treeview.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

    def graficarDouPoint(self,frame,data_1,data_2):
        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(data_1,'o',data_2,'*')

        canvas = FigureCanvasTkAgg(fig,master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(relwidth=1,relheight=1)

    def Entrenar(self,funcion,neurona):

        matriz = []
        YD = []
        for i in range(len(neurona.entradas)):
            fila = []

            for j in range(neurona.entradas.ndim):
                fila.append(neurona.entradas[i,j])

            for j in range(neurona.salidas.ndim):
                fila.append(neurona.salidas[i] if neurona.salidas.ndim==1 else (neurona.salidas[i,j]))
            matriz.append(fila)

        col = []
        for j in range(neurona.entradas.ndim):
            col.append("X"+str(j))

        for j in range(neurona.salidas.ndim):
            col.append("YD"+str(j))

        df_intput_output = pd.DataFrame(matriz, columns=col)

        llenarTabla(tv1,df_intput_output)

        #######################################################
        matriz = []
        for j in range(len(neurona.umbral)):
            matriz.append(neurona.umbral[j])

        df_umbral = pd.DataFrame(matriz)

        llenarTabla(tv2,df_umbral)

        #######################################################
        matriz = []
        for j in range(len(neurona.pesos)):
            matriz.append(neurona.pesos[j])

        df_peso = pd.DataFrame(matriz)

        llenarTabla(tv3,df_peso)

        #######################################################

        iterador = 0
        while True:

            error_patron = []
            contador = 0

            neurona.Entrenar(funcion)

            iterador += 1
            if ((iterador > neurona.numero_iteraciones - 1) or (neurona.error_RMS <= neurona.error)):
                break

        if (neurona.error_RMS <= neurona.error):
            np.savetxt('LF/Data/pesos', neurona.pesos, delimiter =' ')
            np.savetxt('LF/Data/umbral', neurona.umbral, delimiter =' ')
