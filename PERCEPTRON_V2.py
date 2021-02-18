import numpy as np

class Neurona:
    MATRIZ_ENTRADA = np.array([[1,0,1], [0,1,1], [1,1,0]])
    MATRIZ_SALIDA = np.array([[1,0], [0,1], [1,1]])
    MATRIZ_PESOS = np.array([[0.1,-0.5,-0.9], [0.6,0.2,-0.3]])
    MATRIZ_UMBRALES = np.array([0.5, -0.8])

    ENTRADA = 3
    SALIDAS = 2
    PATRONES = 3

    RATA_APRENDIZAJE = 1
    ERROR_ITERACION = 0.1
    NUMERO_ITERACIONES = 1000

    ITERACION_INICIAL = 0

    #METODO PARA ENTRENAR LA NEURONA
    def ENTRENAR():

        #CICLO PARA ITERACIONES
        while True:

            ERROR_PATRON = []



            ITERACION_INICIAL+=1

            #CONDICIONES DE PARADAS
            if((ITERACION_INICIAL > NUMERO_ITERACIONES-1) or (ERMS <= ERROR_ITERACION)):
                break