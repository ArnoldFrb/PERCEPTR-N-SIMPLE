import numpy as np

class Neurona:

    def __init__(self, RATA_APRENDIZAJE, ERROR_ITERACION, NUMERO_ITERACIONES):
        #MATRICES
        self.MATRIZ_ENTRADA = np.array([[1,0,1], [0,1,1], [1,1,0], [0,1,0]])
        self.MATRIZ_SALIDA = np.array([[1,0], [0,1], [1,1], [0,0]])
        self.MATRIZ_PESOS = np.array([[0.1,-0.5,-0.9], [0.6,0.2,-0.3]])
        self.MATRIZ_UMBRALES = np.array([0.5, -0.8])
        #VARIABLES DE CONFIGURACION
        self.RATA_APRENDIZAJE = RATA_APRENDIZAJE
        self.ERROR_ITERACION = ERROR_ITERACION
        self.NUMERO_ITERACIONES = NUMERO_ITERACIONES

    #METODO PARA ENTRENAR LA NEURONA
    def ENTRENAR(self):

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
                
                PATRON_PRESENTADO = (self.MATRIZ_ENTRADA[I,:])
                print("PATRON PRESENTADO")
                print(PATRON_PRESENTADO)

                SALIDA_PATRON = (self.MATRIZ_SALIDA[I,:])
                print("SALIDA DEL PATRON")
                print(SALIDA_PATRON)
                print()

            ITERACION_INICIAL+=1

            #CONDICIONES DE PARADA
            if(ITERACION_INICIAL > 0):
                break

red = Neurona(1, 0.1, 0)
red.ENTRENAR()