import numpy as np
import random as rn 
import pandas as pd

class Entrenador:
    def __init__(self,data = 'LF/Data/prueba.csv'):
        self.dataSet = pd.read_csv(data)

    def GetEntradas(self):
        df = pd.DataFrame()
        for index in self.dataSet.columns:
            if ('x' in index) or ('X' in index):
                df[index] = self.dataSet[index]
        matriz = df.to_numpy()
        return matriz

    def GetSalidas(self):
        df = pd.DataFrame()
        for index in self.dataSet.columns:
            if ('y' in index) or ('Y' in index):
                df[index] = self.dataSet[index]
        matriz = df.to_numpy()
        return matriz
    
    def GenerarPesos(self,salidas,entradas):
        matriz = []
        for n in range(len(salidas[0])):
            fila = []
            for M in range(len(entradas[0])):
                fila.append(round(rn.uniform(-1, 1), 2))
            matriz.append(fila)
        return matriz

    def GenerarUmbrales(self,salidas):
        fila = []
        for n in range(len(salidas[0])):
            fila.append(round(rn.uniform(-1, 1), 2))
        return fila
