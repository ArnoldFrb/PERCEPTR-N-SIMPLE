import random as rn
import numpy as np
from Neurona import *
from TestNeurona import *

class Config:

    #CONSTRUCTOR
    def __init__(self, ARCHIVO_ENTRADA = 'ENTRADAS.TXT', ARCHIVO_SALIDA = 'SALIDAS.TXT', CARPETA = 'PRUEBA'):

        self.MATRIZ_ENTRADA = np.loadtxt('DATA/' + ARCHIVO_ENTRADA)
        self.MATRIZ_SALIDA = np.loadtxt('DATA/' + ARCHIVO_SALIDA)
        self.CARPETA = CARPETA

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
    def ENTRENAR_NEURONA(self, RATA_APRENDIZAJE, ERROR_ITERACION, NUMERO_ITERACIONES, ARC_PESOS, ARC_UMBRALES, FUNCION_SALIDA):
        neuro = Neurona(
            self.MATRIZ_ENTRADA, self.MATRIZ_SALIDA, self.GENERAR_PESOS(), self.GENERAR_UMBRALES(),
            RATA_APRENDIZAJE, ERROR_ITERACION, NUMERO_ITERACIONES, FUNCION_SALIDA
            )
        neuro.ENTRENAR(ARC_PESOS, ARC_UMBRALES, self.CARPETA)
    
    #EJECUTAR SIMULACION
    def SIMULACION(self, ARC_PESOS, ARC_UMBRALES):
        PESOS_TEMPORAL = np.loadtxt("CONFIG/" + self.CARPETA + "/" + ARC_PESOS)
        PESOS_OPTIMOS = np.array([PESOS_TEMPORAL]) if PESOS_TEMPORAL.ndim==1 else PESOS_TEMPORAL

        UMBRALES_TEMPORALES = np.loadtxt("CONFIG/" + self.CARPETA + "/" + ARC_UMBRALES)
        UMBRALES_OPTIMOS = np.array([UMBRALES_TEMPORALES]) if UMBRALES_TEMPORALES.ndim==0 else UMBRALES_TEMPORALES

        simul = TestNeurona(self.MATRIZ_ENTRADA, PESOS_OPTIMOS, UMBRALES_OPTIMOS)
        simul.SIMULAR()

if __name__ == '__main__':
    cf = Config('ENTRADAS.TXT', 'SALIDAS.TXT', 'COMPUERTA_AND')

    print("----------------------")
    print("ESCOJA UNA OPCION")
    print("1 - ENTRENAR RED")
    print("2 - SIMULACION DE LA RED")
    print()
    print("ESCOGER...")
    OP = int(input())

    def ONE():
        print()
        print("----------------------")
        print("ESCOGER LA FUNCION SALIDA")
        print("1 - FUNCION ESCALON")
        print("2 - FUNCION LINEAL")
        print("3 - FUNCION SIGMOIDE")
        print()
        print("ESCOGER...")
        ESCOGER_SALIDA = int(input())

        cf.ENTRENAR_NEURONA(1, 0.1, 5, 'PESOS.TXT', 'UMBRALES.TXT', ESCOGER_SALIDA)

    def TWO():
            cf.SIMULACION('PESOS.TXT', 'UMBRALES.TXT')

    switcher = {
        1: ONE(),
        2: TWO()
    }
    switcher.get(OP, "ERROR")