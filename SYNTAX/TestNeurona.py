import numpy as np

class TestNeurona:

    #CONSTRUCTOR
    def __init__(self, MATRIZ_ENTRADA = [[1,0,1], [0,1,1], [1,1,0]], MATRIZ_PESOS = [[0.1,-0.5,-0.9], [0.6,0.2,-0.3]], MATRIZ_UMBRALES = [0.5, -0.8]):
        #MATRICES
        self.MATRIZ_ENTRADA = MATRIZ_ENTRADA
        self.MATRIZ_PESOS = MATRIZ_PESOS
        self.MATRIZ_UMBRALES = MATRIZ_UMBRALES

    #METODO PARA SIMULAR LA NEURONA
    def SIMULAR(self):

        print("---------------------------")
        print("---------------------------")

        print()
        print("---CONFIGURACION---")
        print()

        print("ENTRADAS: ", len(self.MATRIZ_ENTRADA[0]))
        print("SALIDAS: ", len(self.MATRIZ_PESOS))
        print("PATRONES: ", len(self.MATRIZ_ENTRADA))
        print()
        print("PESOS: ")
        print(self.MATRIZ_PESOS)
        print()
        print("UMBRALES: ")
        print(self.MATRIZ_UMBRALES)

        print("---------------------------")
        print("---------------------------")

        print()
        print("---SIMULACION---")
        print()

        #CICLO ENCARGADO DE PRESENTAR LOS PATRONES
        for I in range(len(self.MATRIZ_ENTRADA)):
                
            print("PATRON: ", I+1)
            print()
            PATRON_PRESENTADO = (self.MATRIZ_ENTRADA[I,:])
            
            print("Xi => YDi")
            print(PATRON_PRESENTADO, " => ", self.FUNCION_ESCALON(self.FUNCION_SOMA(PATRON_PRESENTADO)))
            print("-------------------")
            print()

    #METODO PARA OBTENER LA FUNCION SOMA
    def FUNCION_SOMA(self, PATRON):
        SL = []         #SALIDA DE LA FUNCION SOMA
        for N in range(len(self.MATRIZ_PESOS)):
            SLD = 0     #SUMATORIA DE LA FUNCION SOMA
            for M in range(self.MATRIZ_PESOS.ndim):
                SLD += (PATRON[M] * self.MATRIZ_PESOS[N][M])
            SL.append(SLD - self.MATRIZ_UMBRALES[N])
        return SL

    #METODO PARA OBTENER LA FUNCION ESCALON
    def FUNCION_ESCALON(self, SALIDA_SOMA):
        YR = []
        for N in range(len(SALIDA_SOMA)):
            YR.append(1 if SALIDA_SOMA[N]>=0 else 0)
        return YR