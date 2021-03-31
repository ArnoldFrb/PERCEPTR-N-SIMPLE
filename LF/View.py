from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import numpy as np

import pandas as pd

from Neurona import *

class View:
    def __init__(self):

        def selectEntrada():
            self.fileEntrada = filedialog.askopenfilename()
            ety_entrada.insert(0, self.fileEntrada)

        def selectSalida():
            self.fileSalida = filedialog.askopenfilename()
            ety_salida.insert(0, self.fileSalida)

        def llenarTabla(tv,df):
            tv.delete(*tv.get_children())
            tv["column"] = list(df.columns)
            tv["show"] = "headings"

            for column in tv["columns"]:
                tv.heading(column, text=column) # let the column heading = column name

            df_rows1 = df.to_numpy().tolist() # turns the dataframe into a list of lists
            for row in df_rows1:
                tv.insert("", "end", values=row)
        
        def crearGrid(tv,frame):
            tv.place(relheight=1, relwidth=1)
            treescrolly = Scrollbar(frame, orient="vertical", command=tv.yview)
            treescrollx = Scrollbar(frame, orient="horizontal", command=tv.xview)
            tv.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
            treescrollx.pack(side="bottom", fill="x")
            treescrolly.pack(side="right", fill="y")

        def graficar(frame,v1,v2):
            fig = Figure(figsize=(5, 4), dpi=100)
            fig.add_subplot(111).plot(self.v1, self.v2)

            canvas = FigureCanvasTkAgg(master=frame)
            canvas.draw()
            canvas.get_tk_widget().place(relwidth=1,relheight=1)

        def Entrenar(funcion):
            

            self.neurona = Neurona(self.fileEntrada, self.fileSalida)

            matriz = []

            for i in range(len(self.neurona.entradas)):
                fila = []

                for j in range(self.neurona.entradas.ndim):
                    fila.append(self.neurona.entradas[i,j])

                for j in range(self.neurona.salidas.ndim):
                    fila.append(self.neurona.salidas[i] if self.neurona.salidas.ndim==1 else (self.neurona.salidas[i,j]))

                matriz.append(fila)

            col = []
            for j in range(self.neurona.entradas.ndim):
                col.append("X"+str(j))

            for j in range(self.neurona.salidas.ndim):
                col.append("YD"+str(j))

            df_intput_output = pd.DataFrame(matriz, columns=col)

            llenarTabla(tv1,df_intput_output)

            #######################################################
            matriz = []
            for j in range(len(self.neurona.umbral)):
                matriz.append(self.neurona.umbral[j])

            df_umbral = pd.DataFrame(matriz)

            llenarTabla(tv2,df_umbral)

            #######################################################
            matriz = []
            for j in range(len(self.neurona.pesos)):
                matriz.append(self.neurona.pesos[j])
    
            df_peso = pd.DataFrame(matriz)

            llenarTabla(tv3,df_peso)

            #######################################################

            iterador = 0
            while True:

                error_patron = []
                contador = 0

                self.neurona.Entrenar(funcion)

                iterador += 1
                if ((iterador > self.neurona.numero_iteraciones - 1) or (self.neurona.error_RMS <= self.neurona.error)):
                    break

            if (self.neurona.error_RMS <= self.neurona.error):
                np.savetxt('Data/pesos', self.neurona.pesos, delimiter =' ')
                np.savetxt('Data/umbral', self.neurona.umbral, delimiter =' ')
            
            #######################################################
            matriz = []
            for j in range(len(self.neurona.umbral)):
                matriz.append(self.neurona.umbral[j])

            df_umbral = pd.DataFrame(matriz)

            llenarTabla(tv5,df_umbral)

            #######################################################
            matriz = []
            for j in range(len(self.neurona.pesos)):
                matriz.append(self.neurona.pesos[j])
    
            df_peso = pd.DataFrame(matriz)

            llenarTabla(tv4,df_peso)

            #######################################################

            lbl_error = Label(self.root, text='Error RMS:'+str(self.neurona.error_RMS))

            #graficar(frame_grafica_simulacion)
            #graficar(frame_grafica_error)

        
        self.root = Tk()
        self.root.title('Perceptron Simple')
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(),self.root.winfo_screenheight()))
        
        frame_input_output = Frame(self.root)
        frame_input_output.place(relx=.01,rely=.01,relwidth=.33,relheight=.11)

        btnSelectEntradas = Button(frame_input_output, text="Cargar entrada", command=lambda:selectEntrada())
        btnSelectEntradas.place(relx=.05,rely=.01,relwidth=.25,relheight=.30)

        ety_entrada = Entry(frame_input_output, width=50)
        ety_entrada.place(relx=.35,rely=.01,relwidth=.64,relheight=.30)

        btnSelectSalidas = Button(frame_input_output, text="Cargar salida", command=lambda:selectSalida())
        btnSelectSalidas.place(relx=.05,rely=.34,relwidth=.25,relheight=.30)

        ety_salida = Entry(frame_input_output, width=50)
        ety_salida.place(relx=.35,rely=.34,relwidth=.64,relheight=.30)

        combo = Combobox(frame_input_output)
        combo['values']= ('Funcion Escalon','Funcion Lineal','Funcion Sigma')
        combo.current(0)
        combo.place(relx=.35,rely=.67,relwidth=.64,relheight=.30)

        btnEntrenar = Button(frame_input_output, text="Entrenar", command=lambda:Entrenar(combo.get()))
        btnEntrenar.place(relx=.05,rely=.67,relwidth=.25,relheight=.30)

        ###################################################################

        frame_view_input_output = LabelFrame(self.root, text="Entradas y salidas")
        frame_view_input_output.place(relx=.01,rely=.12,relwidth=.33,relheight=.33)

        tv1 = Treeview(frame_view_input_output)
        crearGrid(tv1,frame_view_input_output)

        ###################################################################

        frame_view_umbral = LabelFrame(self.root, text="Umbral")
        frame_view_umbral.place(relx=.01,rely=.47,relwidth=.16,relheight=.16)

        tv2 = Treeview(frame_view_umbral)
        crearGrid(tv2,frame_view_umbral)

        ###################################################################

        frame_view_Peso = LabelFrame(self.root, text="Pesos")
        frame_view_Peso.place(relx=.18,rely=.47,relwidth=.16,relheight=.16)

        tv3 = Treeview(frame_view_Peso)
        crearGrid(tv3,frame_view_Peso)

        ###################################################################


        frame_view_new_umbral = LabelFrame(self.root, text="Nuevos Umbral")
        frame_view_new_umbral.place(relx=.01,rely=.65,relwidth=.16,relheight=.16)

        tv5 = Treeview(frame_view_new_umbral)
        crearGrid(tv5,frame_view_new_umbral)

        ###################################################################

        frame_view_new_Peso = LabelFrame(self.root, text="Nuevos Pesos")
        frame_view_new_Peso.place(relx=.18,rely=.65,relwidth=.16,relheight=.16)

        tv4 = Treeview(frame_view_new_Peso)
        crearGrid(tv4,frame_view_new_Peso)

        ###################################################################

        frame_grafica_simulacion = LabelFrame(self.root, text="Grafica YD vs YR")
        frame_grafica_simulacion.place(relx=.36,rely=.01,relwidth=.60,relheight=.45)

        ###################################################################

        frame_grafica_error = LabelFrame(self.root, text="Grafica del error")
        frame_grafica_error.place(relx=.36,rely=.50,relwidth=.60,relheight=.45)


        self.root.mainloop()

view = View()