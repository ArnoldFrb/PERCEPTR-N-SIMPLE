from tkinter import *

class Views:

    def __init__(self, window):
        self.wind = window
        self.wind.title("PERCEPTRON")
        self.wind.resizable(0,0)
        self.wind.geometry("1100x600")  

        #CREAR CONTENDOR FRAME
        frame = LabelFrame(self.wind, text = 'CONFIGURACION DE LA RED')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 10, padx=10)
        
        #INPUT ENTRADAS
        Label(frame, text = 'ARCH. ENTRADAS: ').grid(row=1, column=0)
        self.ENTRADAS = Entry(frame)
        self.ENTRADAS.grid(row=1, column=1)

        Label(frame, text = '').grid(row=2, column=0)
        Label(frame, text = '').grid(row=2, column=1)

        #INPUT SALIDAS
        Label(frame, text = 'ARCH. SALIDAS: ').grid(row=3, column=0)
        self.SALIDAS = Entry(frame)
        self.SALIDAS.grid(row=3, column=1)

        #INFORMACION DE CONFIGURACION DE LA RED
        Label(frame, text = '  ').grid(row=1, column=2)
        Label(frame, text = '  ').grid(row=2, column=2)
        Label(frame, text = '  ').grid(row=3, column=2)

        Label(frame, text = 'ENTRADAS: ').grid(row=1, column=3)
        Label(frame, text = 'SALIDAS: ').grid(row=2, column=3)
        Label(frame, text = 'PATRONES: ').grid(row=3, column=3)

        Label(frame, text = '').grid(row=1, column=5)
        Label(frame, text = '').grid(row=2, column=5)
        Label(frame, text = '').grid(row=3, column=5)

        Label(frame, text = '  ').grid(row=1, column=5)
        Label(frame, text = '  ').grid(row=2, column=5)
        Label(frame, text = '  ').grid(row=3, column=5)

        Label(frame, text = 'RATA DE APRENDIZAJE: ').grid(row=1, column=6)
        self.RARA_APRENDIZAJE = Entry(frame)
        self.RARA_APRENDIZAJE.grid(row=1, column=7)

        Label(frame, text = 'ERROR MAXIMO PERMIT: ').grid(row=2, column=6)
        self.ERROR_MAXIMO_PERMITIDO = Entry(frame)
        self.ERROR_MAXIMO_PERMITIDO.grid(row=2, column=7)

        Label(frame, text = 'NUMERO DE ITERACIONES: ').grid(row=3, column=6)
        self.NUMERO_ITERACIONES = Entry(frame)
        self.NUMERO_ITERACIONES.grid(row=3, column=7)

if __name__ == '__main__':
    window = Tk()
    Views(window)
    window.mainloop()

"""
raiz = Tk()
raiz.title("PERCEPTRON")
raiz.resizable(0,0)
raiz.geometry("1100x600")
raiz.mainloop()
"""