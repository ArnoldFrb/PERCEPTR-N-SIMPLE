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
        Label(frame, text = 'ENTRADAS: ').grid(row=1, column=0)
        self.ENTRADAS = Entry(frame)
        self.ENTRADAS.grid(row=1, column=1)

        Label(frame, text = '').grid(row=2, column=0)
        Label(frame, text = '').grid(row=2, column=1)

        #INPUT SALIDAS
        Label(frame, text = 'SALIDAS: ').grid(row=3, column=0)
        self.SALIDAS = Entry(frame)
        self.SALIDAS.grid(row=3, column=1)

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