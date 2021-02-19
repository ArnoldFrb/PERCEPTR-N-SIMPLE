import numpy as np

class Neurona:

    MATRIZ_ENTRADA = np.array([[1,0,1], [0,1,1], [1,1,0], [0,1,0]])
    MATRIZ_SALIDA = np.array([[1,0], [0,1], [1,1], [0,0]])
    MATRIZ_PESOS = np.array([[0.1,-0.5,-0.9], [0.6,0.2,-0.3]])
    MATRIZ_UMBRALES = np.array([0.5, -0.8])

    RATA_APRENDIZAJE = 1
    ERROR_ITERACION = 0.1
    NUMERO_ITERACIONES = 1

    ITERACION_INICIAL = 0

    #METODO PARA ENTRENAR LA NEURONA
    def ENTRENAR():

        print()
        print("---ENTRENAMIENTO---")
        print()

        #CICLO PARA ITERACIONES
        while True:

            print("---------------------------")
            print("ITERACION: ", Neurona.ITERACION_INICIAL+1)
            print("---------------------------")

            ERROR_PATRON = []

            #CICLO ENCARGADO DE RECORRER LOS PATRONES
            for I in range(len(Neurona.MATRIZ_ENTRADA)):
                
                PATRON_PRESENTADO = (Neurona.MATRIZ_ENTRADA[I,:])
                print(PATRON_PRESENTADO)


            Neurona.ITERACION_INICIAL+=1

            #CONDICIONES DE PARADA
            if(Neurona.ITERACION_INICIAL > 0):
                break

Neurona.ENTRENAR()