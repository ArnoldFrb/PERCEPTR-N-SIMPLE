import numpy as np
import random as rn 

class Config:
    def __init__(self, archivo_entrada = 'Data/entradas', archivo_salida = 'Data/salidas'):
        self.matriz_entrada = np.loadtxt(archivo_entrada)
        self.matriz_salida = np.loadtxt(archivo_salida)

    def GetEntradas(self):
        return self.matriz_entrada

    def GetSalidas(self):
        return self.matriz_salida
    
    def GenerarPesos(self):
        matriz = []
        for n in range(self.matriz_salida.ndim):
            fila = []
            for M in range(len(self.matriz_entrada[0])):
                fila.append(round(rn.uniform(-1, 1), 2))
            matriz.append(fila)
        return matriz

    def GenerarUmbrales(self):
        fila = []
        for n in range(self.matriz_salida.ndim):
            fila.append(round(rn.uniform(-1, 1), 2))
        return fila