import random as rn
import numpy as np
from TestNeurona import *

class ConfigSimulacion:

    #CONSTRUCTOR
    def __init__(self, ARCHIVO_ENTRADA = 'ENTRADAS.TXT', CARPETA = 'PRUEBA', FUNCION_SALIDA = 1):

        self.MATRIZ_ENTRADA = np.loadtxt('DATA/' + ARCHIVO_ENTRADA)
        self.CARPETA = CARPETA
        self.FUNCION_SALIDA = FUNCION_SALIDA
    
    #EJECUTAR SIMULACION
    def SIMULACION(self):
        PESOS_TEMPORAL = np.loadtxt("CONFIG/" + self.CARPETA + "/" + self.NOMBRE_SALIDAS() + "/PESOS.TXT")
        PESOS_OPTIMOS = np.array([PESOS_TEMPORAL]) if PESOS_TEMPORAL.ndim==1 else PESOS_TEMPORAL

        UMBRALES_TEMPORALES = np.loadtxt("CONFIG/" + self.CARPETA + "/" + self.NOMBRE_SALIDAS() + "/UMBRALES.TXT")
        UMBRALES_OPTIMOS = np.array([UMBRALES_TEMPORALES]) if UMBRALES_TEMPORALES.ndim==0 else UMBRALES_TEMPORALES

        simul = TestNeurona(self.MATRIZ_ENTRADA, PESOS_OPTIMOS, UMBRALES_OPTIMOS)
        simul.SIMULAR()
    
    #NOMBRE DE LA FUNCION SALIDA
    def NOMBRE_SALIDAS(self):
        switcher = {
            1: 'ESCALON',
            2: 'LINEAL',
            3: 'SIGMOIDE'
        }
        return switcher.get(self.FUNCION_SALIDA, "ERROR")

if __name__ == '__main__':
    cfs = ConfigSimulacion('ENTRADAS.TXT', 'COMPUERTA_AND', 1)
    cfs.SIMULACION()