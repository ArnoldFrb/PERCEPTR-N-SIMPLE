import numpy as np

class Neurona:
    X = np.array([[1,0,1], [0,1,1], [1,1,0]])               #MATRIZ ENTRADAS

    YD = np.array([[1,0], [0,1], [1,1]])                    #MATRIZ SALIDAS

    PESOS = np.array([[0.1,-0.5,-0.9], [0.6,0.2,-0.3]])     #MATRIZ PESOS

    UMBRALES = np.array([0.5, -0.8])                        #MATRIZ UMBRAL

    M = 3       #ENTREDAS
    N = 2       #SALIDAS
    P = 3       #PATRONES

    RA = 1      #RATA DE APRENDIZAJE
    ER = 0.1    #ERROR LINEAL
    NI = 1000   #NUMERO DE ITERACIONES

    IT = 0      #ITERACION INICIAL

    def ENTRENAR():
        