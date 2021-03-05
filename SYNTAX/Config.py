import random as rn
import numpy as np
from Neurona import *

class Config:

    #CONSTRUCTOR
    def __init__(self, ARCHIVO_ENTRADA = 'ENTRADAS.TXT', ARCHIVO_SALIDA = 'SALIDAS.TXT'):

        self.MATRIZ_ENTRADA = np.loadtxt('DATA/' + ARCHIVO_ENTRADA)
        self.MATRIZ_SALIDA = np.loadtxt('DATA/' + ARCHIVO_SALIDA)

    #METODO PARA GENERAR PESOS
    def GENERAR_PESOS(self):
        MATRIZ = []
        for N in range(self.MATRIZ_SALIDA.ndim):
            FILA = []
            for M in range(len(self.MATRIZ_ENTRADA[0])):
                FILA.append(round(rn.uniform(-1, 1), 2))
            MATRIZ.append(FILA)
        return MATRIZ

    #METODO PARA GENERAR UMBRALES
    def GENERAR_UMBRALES(self):
        FILA = []
        for N in range(self.MATRIZ_SALIDA.ndim):
            FILA.append(round(rn.uniform(-1, 1), 2))
        return FILA

    #EJECUTAR NEURONA
    def MAIN(self, RATA_APRENDIZAJE, ERROR_ITERACION, NUMERO_ITERACIONES):
        neuro = Neurona(
            self.MATRIZ_ENTRADA, self.MATRIZ_SALIDA, self.GENERAR_PESOS(), self.GENERAR_UMBRALES(),
            RATA_APRENDIZAJE, ERROR_ITERACION, NUMERO_ITERACIONES
            )
        neuro.ENTRENAR()

if __name__ == '__main__':
    cf = Config('ENTRADAS.TXT', 'SALIDAS.TXT')
    cf.MAIN(1, 0.1, 1000)