import numpy as np
import os
import errno
import math

class Neurona:

    #CONSTRUCTOR
    def __init__(self, MATRIZ_ENTRADA = [[1,0,1], [0,1,1], [1,1,0]], MATRIZ_SALIDA = [[1,0], [0,1], [1,1]], MATRIZ_PESOS = [[0.1,-0.5,-0.9], [0.6,0.2,-0.3]], MATRIZ_UMBRALES = [0.5, -0.8], RATA_APRENDIZAJE = 1, ERROR_MAXIMO = 0.1, NUMERO_ITERACIONES = 0, FUNCION_SALIDA = 1):
        #MATRICES
        self.MATRIZ_ENTRADA = MATRIZ_ENTRADA
        self.MATRIZ_SALIDA = MATRIZ_SALIDA
        self.MATRIZ_PESOS = MATRIZ_PESOS
        self.MATRIZ_UMBRALES = MATRIZ_UMBRALES
        #VARIABLES DE CONFIGURACION
        self.RATA_APRENDIZAJE = RATA_APRENDIZAJE
        self.ERROR_MAXIMO = ERROR_MAXIMO
        self.NUMERO_ITERACIONES = NUMERO_ITERACIONES
        self.FUNCION_SALIDA = FUNCION_SALIDA

    #METODO PARA ENTRENAR LA NEURONA
    def ENTRENAR(self, ARC_PESOS, ARC_UMBRALES, CARPETA):

        print("---------------------------")
        print("---------------------------")

        print()
        print("---CONFIGURACION---")
        print()

        print("ENTRADAS: ", len(self.MATRIZ_ENTRADA[0]))
        print("SALIDAS: ", self.MATRIZ_SALIDA.ndim)
        print("PATRONES: ", len(self.MATRIZ_ENTRADA))
        print()
        print("RATA DE APRENDIZAJE: ", self.RATA_APRENDIZAJE)
        print("ERROR MAXIMO PERMITIDO: ", self.ERROR_MAXIMO)
        print("NUMERO ITERACIONES: ", self.NUMERO_ITERACIONES)
        print()
        print("PESOS INICIALES: ")
        print(self.MATRIZ_PESOS)
        print()
        print("UMBRALES INICIALES: ")
        print(self.MATRIZ_UMBRALES)

        print("---------------------------")
        print("---------------------------")

        print()
        print("---ENTRENAMIENTO---")
        print()

        #CICLO PARA ITERACIONES
        ITERACION_INICIAL = 0
        while True:

            print("---------------------------")
            print("ITERACION: ", ITERACION_INICIAL+1)
            print("---------------------------")

            ERROR_PATRON = []

            #CICLO ENCARGADO DE PRESENTAR LOS PATRONES
            for I in range(len(self.MATRIZ_ENTRADA)):
                
                print("PATRON: ", I+1)
                print()
                PATRON_PRESENTADO = (self.MATRIZ_ENTRADA[I,:])
                print("PATRON PRESENTADO")
                print(PATRON_PRESENTADO)

                SALIDA_PATRON = np.array([self.MATRIZ_SALIDA[I]]) if self.MATRIZ_SALIDA.ndim==1 else (self.MATRIZ_SALIDA[I,:])
                print("SALIDA DEL PATRON")
                print(SALIDA_PATRON)
                print()

                print("FUNCION SOMA")
                print(self.FUNCION_SOMA(PATRON_PRESENTADO))
                print()

                print("FUNCION SALIDA")
                print(self.FUNCION_SALIDAS(self.FUNCION_SOMA(PATRON_PRESENTADO)))
                print()

                print("ERROR LINIAL")
                print(self.FUNCION_ERROR_LINEAL(SALIDA_PATRON, self.FUNCION_SALIDAS(self.FUNCION_SOMA(PATRON_PRESENTADO))))
                print()

                print("ERRORES PATRONES")
                print((np.abs(self.FUNCION_ERROR_LINEAL(SALIDA_PATRON, self.FUNCION_SALIDAS(self.FUNCION_SOMA(PATRON_PRESENTADO)))).sum()) / self.MATRIZ_SALIDA.ndim)
                print()

                ERROR_PATRON.append((np.abs(self.FUNCION_ERROR_LINEAL(SALIDA_PATRON, self.FUNCION_SALIDAS(self.FUNCION_SOMA(PATRON_PRESENTADO)))).sum()) / self.MATRIZ_SALIDA.ndim)

                print("NUEVOS PESOS")
                self.ACTUALIZAR_PESOS(PATRON_PRESENTADO, self.FUNCION_ERROR_LINEAL(SALIDA_PATRON, self.FUNCION_SALIDAS(self.FUNCION_SOMA(PATRON_PRESENTADO))))
                print(self.MATRIZ_PESOS)
                print()

                print("NUEVOS PESOS")
                self.ACTUALIZAR_UMBRALES(self.FUNCION_ERROR_LINEAL(SALIDA_PATRON, self.FUNCION_SALIDAS(self.FUNCION_SOMA(PATRON_PRESENTADO))))
                print(self.MATRIZ_UMBRALES)
                print()
                print("---------------------------")

            print("---------------------------")
            #METODO PARA OBTENER EL ERROR DEL PATRON
            print("ERRORES PATRONES")
            print(ERROR_PATRON)
            print()

            #METODO PARA OBTENER EL ERROR DE LA ITERACION
            print("ERROR DE LA ITERACION")
            ERROR_RMS = (np.sum(ERROR_PATRON)) / len(self.MATRIZ_ENTRADA)
            print(ERROR_RMS)
            print()

            ITERACION_INICIAL+=1

            #CONDICIONES DE PARADA
            if((ITERACION_INICIAL > self.NUMERO_ITERACIONES-1) or (ERROR_RMS <= self.ERROR_MAXIMO)):
                break
        
        if(ERROR_RMS <= self.ERROR_MAXIMO):
            try:
                os.mkdir('CONFIG/' + CARPETA)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            
            np.savetxt("CONFIG/" + CARPETA + "/" + ARC_PESOS, self.MATRIZ_PESOS)
            np.savetxt("CONFIG/" + CARPETA + "/" + ARC_UMBRALES, self.MATRIZ_UMBRALES)
            
            print("PESOS OPTIMOS: ")
            print(self.MATRIZ_PESOS)
            print()
            print("UMBRALES OPTIMOS: ")
            print(self.MATRIZ_UMBRALES)
            print()
        
        print("NUMERO DE ITERACIONES REALIZADAS: ", ITERACION_INICIAL)
        print()

    #METODO PARA OBTENER LA FUNCION SOMA
    def FUNCION_SOMA(self, PATRON):
        SL = []         #SALIDA DE LA FUNCION SOMA
        for N in range(len(self.MATRIZ_PESOS)):
            SLD = 0     #SUMATORIA DE LA FUNCION SOMA
            for M in range(len(self.MATRIZ_PESOS[0])):
                SLD += (PATRON[M] * self.MATRIZ_PESOS[N][M])
            SL.append(SLD - self.MATRIZ_UMBRALES[N])
        return SL

    #METODO PARA OBTENER EL ERROR LINEAL
    def FUNCION_ERROR_LINEAL(self, SALIDA_PATRON, ESCALON):
        EL = []          #ERROR LINEAL
        for N in range(len(ESCALON)):
            EL.append(SALIDA_PATRON[N] - ESCALON[N])
        return EL
    
    #METODO PARA ACTUALIZAR PESOS
    def ACTUALIZAR_PESOS(self, PATRON_PRESENTADO, ERROR_LINEAL):
        for N in range(len(self.MATRIZ_PESOS)):
            for M in range(len(self.MATRIZ_PESOS[0])):
                self.MATRIZ_PESOS[N][M] += (self.RATA_APRENDIZAJE * ERROR_LINEAL[N] * PATRON_PRESENTADO[M])

    #METODO PARA ACTUALIZAR UMBRALES
    def ACTUALIZAR_UMBRALES(self, ERROR_LINEAL):
        for N in range(len(self.MATRIZ_UMBRALES)):
            self.MATRIZ_UMBRALES[N] += (self.RATA_APRENDIZAJE * ERROR_LINEAL[N] * 1)

    def FUNCION_SALIDAS(self, SALIDA_SOMA):
        switcher = {
            1: self.FUNCION_ESCALON(SALIDA_SOMA),
            2: self.FUNCION_LINEAL(SALIDA_SOMA),
            3: self.FUNCION_SIGMOIDE(SALIDA_SOMA)
        }
        return switcher.get(self.FUNCION_SALIDA, "ERROR")

    #METODO PARA OBTENER LA FUNCION ESCALON
    def FUNCION_ESCALON(self, SALIDA_SOMA):
        YR = []
        for N in range(len(SALIDA_SOMA)):
            YR.append(1 if SALIDA_SOMA[N]>=0 else 0)
        return YR

    #METODO PARA OBTENER LA FUNCION SIGMOIDE
    def FUNCION_SIGMOIDE(self, SALIDA_SOMA):
        YR = []
        for N in range(len(SALIDA_SOMA)):
            YR.append(1 / (1 + np.exp(-SALIDA_SOMA[N])))
        return YR

    #METODO PARA OBTENER LA FUNCION LINEAL
    def FUNCION_LINEAL(self, SALIDA_SOMA):
        YR = SALIDA_SOMA
        return YR