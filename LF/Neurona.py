import numpy as np
from Config import *

class Neurona:
    def __init__(self,rata_aprendizaje = 1, error = 0.1, numero_iteraciones = 1000):
        cfg = Config()

        self.entradas = cfg.GetEntradas()
        self.salidas = cfg.GetSalidas()
        self.pesos = cfg.GenerarPesos()
        self.umbral = cfg.GenerarUmbrales()
        self.rata_aprendizaje = rata_aprendizaje
        self.error = error
        self.numero_iteraciones = numero_iteraciones

    def CalcularSalidaResultante(self, entrada, pesos, umbral):
        salida_resultante = []
        iterador = 0
        for peso in pesos:
            salida_resultante.append((entrada @ peso)-umbral[iterador])
            iterador += 1
        return salida_resultante

    def FuncionEscalon(self, salida_resultante):
        salida = []
        for escalon in salida_resultante:
            salida_resultante_new = 1 if escalon >= 0 else 0
            salida.append(salida_resultante_new)
        return salida

    def CalcularErrorLineal(self, salidas, salida, iterador):
        return np.subtract(salidas[iterador], salida)

    def CalcularErrorPatron(self, error_lineal):
        return abs(error_lineal).sum()/len(error_lineal)

    def NuevoPeso(self, entrada, pesos, rata, error_lineal):
        for j in range(len(pesos)) :
            for i in range(len(pesos[0])) :
                pesos[j][i] += rata * error_lineal[j] * entrada[i]

    def NuevoUmbral(self, umbral, rata, error_lineal):
        for j in range(len(umbral)) :
            umbral[j] += rata*error_lineal[j]

    def CalcularErrorRMS(self, error_patron):
        return np.abs(error_patron).sum()/len(error_patron)

    def Entrenar(self):

        error_lineal = []
        iterador = 0

        while True:

            error_patron = []
            contador = 0
            
            for entrada in self.entradas:

                salida_resultante = self.CalcularSalidaResultante(entrada, self.pesos, self.umbral)

                salida = self.FuncionEscalon(salida_resultante)

                error_lineal = self.CalcularErrorLineal(self.salidas, salida, contador)

                error_patron.append(self.CalcularErrorPatron(error_lineal))

                self.NuevoPeso(entrada, self.pesos, self.rata_aprendizaje, error_lineal)

                self.NuevoUmbral(self.umbral, self.rata_aprendizaje, error_lineal)

                error_RMS = self.CalcularErrorRMS(error_patron)

                contador += 1

            iterador += 1            

            if ((iterador > self.numero_iteraciones - 1) or (error_RMS <= self.error)) :
                break
        
        if (error_RMS <= self.error):
            np.savetxt('Data/pesos', self.pesos, delimiter =' ')
            np.savetxt('Data/umbral', self.umbral, delimiter =' ')