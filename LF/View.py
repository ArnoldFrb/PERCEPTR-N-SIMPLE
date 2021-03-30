from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class View:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("500x600")
        self.ventana.title('Perceptron Simple')

        lbl_1 = Label(self.ventana, text="Función")
        lbl_1.grid(column=1, row=1)

        combo = Combobox(self.ventana)
        combo['values']= ('Escalon','Soma','s','ss')
        combo.current(0)
        combo.grid(column=1, row=2)

        bar = Progressbar(self.ventana, length=390)
        bar['value'] = 33
        bar.grid(column=1, row=3)

        def selectEntrada():
            fileEntrada = filedialog.askopenfilename()

        btnSelectEntradas = Button(self.ventana, text="Click Me", command=selectEntrada)
        btnSelectEntradas.grid(column=1, row=4)

        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0,3,.01)
        fig.add_subplot(111).plot(t,2 *np.sin(2*np.pi * t))

        canvas = FigureCanvasTkAgg(fig, master=self.ventana)
        canvas.draw()
        canvas.get_tk_widget().grid(column=1, row=5)

    def show(self):
        self.ventana.mainloop()

    def selectSalidas(self):
        file = filedialog.askopenfilename()

view = View()

view.show()