from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from Neurona import *

class View:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("1000x600")
        self.ventana.title('Perceptron Simple')

        #Label(self.ventana, text="Función").grid(column=1, row=1)

        #combo = Combobox(self.ventana)
        #combo['values']= ('Escalon','Soma','s','ss')
        #combo.current(0)
        #combo.grid(column=1, row=2)

        

        ety_entrada = Entry(self.ventana, width=100)
        ety_entrada.grid(column=1, row=0)

        def selectEntrada():
            self.fileEntrada = filedialog.askopenfilename()
            ety_entrada.insert(0,self.fileEntrada)
        
        btnSelectEntradas = Button(self.ventana, text="Registrar entrada", command=lambda:selectEntrada())
        btnSelectEntradas.grid(column=0, row=0)

        ety_salida = Entry(self.ventana, width=100)
        ety_salida.grid(column=1, row=1)

        def selectSalida():
            self.fileSalida = filedialog.askopenfilename()
            ety_salida.insert(0,self.fileSalida)
            

        btnSelectEntradas = Button(self.ventana, text="Registrar salida", command=lambda:selectSalida())
        btnSelectEntradas.grid(column=0, row=1)

        def Entrenar():

            bar['value'] = 0 

            neurona = Neurona(self.fileEntrada, self.fileSalida)

            iterador = 0

            while True:

                error_patron = []
                contador = 0
                
                neurona.Entrenar()

                iterador += 1    

                bar['value'] = int((iterador/neurona.numero_iteraciones)*100)        

                if ((iterador > neurona.numero_iteraciones - 1) or (neurona.error_RMS <= neurona.error)) :
                    bar['value'] = 100
                    break
            
            if (neurona.error_RMS <= neurona.error):
                np.savetxt('Data/pesos', neurona.pesos, delimiter =' ')
                np.savetxt('Data/umbral', neurona.umbral, delimiter =' ')
                
            lbl_resultados = Label(self.ventana, text=neurona.error_RMS)
            lbl_resultados.grid(column=0, row=4)

        btnEntrenar = Button(self.ventana, text="Entrenar", command=lambda:Entrenar())
        btnEntrenar.grid(column=0, row=2)

        bar = Progressbar(self.ventana, length=390)
        bar.grid(columnspan=2, row=3)

        
        #

        #fig = Figure(figsize=(5, 4), dpi=100)
        #t = np.arange(0,3,.01)
        #fig.add_subplot(111).plot(t,2 *np.sin(2*np.pi * t))

        #canvas = FigureCanvasTkAgg(fig, master=self.ventana)
        #canvas.draw()
        #canvas.get_tk_widget().grid(column=1, row=5)

    def show(self):
        self.ventana.mainloop()

view = View()
view.show()