import numpy as np
import random as rn 
import pandas as pd

class Entrenamiento:
    def __init__(self,data = 'Data/data'):
        self.df_entrada = pd.read_cvg(data, delimiter='', sheet_name='entrada')
        self.df_salida = pd.read_cvg(data, delimiter='', sheet_name='salida')

    def GetEntradas(self):
        matriz = self.df_entrada.to_numpy()
        return matriz

    def GetSalidas(self):
        matriz = self.df_salida.to_numpy()
        return matriz
    
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