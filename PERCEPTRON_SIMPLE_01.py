import numpy as np

class Neurona:
    def __init__(self):
        self.X = np.array([[1,0,1], [0,1,1], [1,1,0]])
        self.YD = np.array([[1,0], [0,1], [1,1]])
        self.PESOS = np.array([[0.1,-0.5,-0.9], [0.6,0.2,-0.3]])
        self.UMBRAL = np.array([0.5, -0.8])
        self.RATA = 1      #RATA DE APRENDIZAJE
        self.ERROR = 0.1    #ERROR LINEAL
        self.NUMERO_ITERACIONES = 3

    def CALCULAR_YR(self, ENTRADA, PESOS, UMBRAL):
        YR = []
        IT = 0
        for PESO in PESOS:
            YR.append((ENTRADA @ PESO)-UMBRAL[IT])
            IT += 1
        return YR

    def FUNCION_ESCALON(self, YR):
        SALIDA = []
        for ESCALON in YR:
            if ESCALON >= 0:
                SALIDA.append(1)
            else:
                SALIDA.append(0)
        return SALIDA

    def CALCULAR_ERROR_LINEAL(self, YD, SALIDA, CONTADOR):
        return np.subtract(YD[CONTADOR], SALIDA)

    def CALCULAR_ERROR_PATRON(self, ERROR_LINEAL):
        return abs(ERROR_LINEAL).sum()/len(ERROR_LINEAL)

    def NEW_PESO(self, ENTRADA, PESOS, RATA, ERROR_LINEAL):
        for j in range(len(PESOS)) :
            for i in range(len(PESOS[0])) :
                PESOS[j][i] += RATA * ERROR_LINEAL[j] * ENTRADA[i]

    def NEW_UMBRAL(self, UMBRAL, RATA, ERROR_LINEAL):
        for j in range(len(UMBRAL)) :
            UMBRAL[j] += RATA*ERROR_LINEAL[j]

    def CALCULAR_ERROR_RMS(self, ERROR_PATRON):
        return np.abs(ERROR_PATRON).sum()/len(ERROR_PATRON)

    def ENTRENAR(self):

        ERROR_LINEAL = [] #NUMERO DE ITERACIONES
        ITERATE = 0  #ITERACION INICIAL

        while True:

            ERROR_PATRON = []   #ERROR PATRON
            CONTADOR = 0

            print("---------------------------")
            print("ITERACION: ",ITERATE + 1)
            print("---------------------------")
            
            #CICLO PARA ITERACIONES
            for ENTRADA in self.X:
                print("PATRON: ",CONTADOR + 1,"\n")
                print("PATRON PRESENTADO",ENTRADA,"\n")

                YR = self.CALCULAR_YR(ENTRADA, self.PESOS, self.UMBRAL)
                print("YR",YR,"\n")

                SALIDA = self.FUNCION_ESCALON(YR)
                print("SALIDA DEL PATRON",SALIDA,"\n")

                ERROR_LINEAL = self.CALCULAR_ERROR_LINEAL(self.YD, SALIDA, CONTADOR)
                print("ERROR_LINEAL",ERROR_LINEAL,"\n")

                ERROR_PATRON.append(self.CALCULAR_ERROR_PATRON(ERROR_LINEAL))
                print("ERROR_PATRON",ERROR_PATRON,"\n")

                self.NEW_PESO(ENTRADA, self.PESOS, self.RATA, ERROR_LINEAL)
                print("PESOS",self.PESOS,"\n")

                self.NEW_UMBRAL(self.UMBRAL, self.RATA, ERROR_LINEAL)
                print("UMBRAL",self.UMBRAL,"\n")

                print("---------------------------")

                ERROR_RMS = self.CALCULAR_ERROR_RMS(ERROR_PATRON)
                CONTADOR += 1

            ITERATE += 1

            print("---------------------------")
            print("ERROR DE LOS PATRONES",ERROR_PATRON,"\n")
            print("ERROR DE LA ITERACION",ERROR_RMS,"\n")

            if ((ITERATE > self.NUMERO_ITERACIONES - 1) or (ERROR_RMS <= self.ERROR)) :
                break

red = Neurona()
red.ENTRENAR()