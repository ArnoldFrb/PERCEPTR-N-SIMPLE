import numpy as np
import random as rn

archivo_entrada = 'entradas'

archivo_salida = 'salidas'

X =  np.loadtxt('Data/' + archivo_entrada)

YD = np.loadtxt('Data/' + archivo_salida)

PESOS = []

UMBRAL = []

RATA = 1    

ERROR = 0.1

NUMERO_ITERACIONES = 10

ERROR_LINEAL = []

ITERATE = 0 

funcion = '0'

for n in range(YD.ndim):
    fila = []
    for M in range(len(X[0])):
        fila.append(round(rn.uniform(-1, 1), 2))
    PESOS.append(fila)


for n in range(YD.ndim):
    UMBRAL.append(round(rn.uniform(-1, 1), 2))

def FuncionSoma(self, patron):
    salida = []   
    for i in range(self.salidas.ndim):
        for j in range(len(patron)):
            suma_funcion_soma = (patron[j] * self.pesos[i][j]) - self.umbral[i]
            salida.append(suma_funcion_soma)
    return salida

while True:

    ERROR_PATRON = []   #ERROR PATRON
    CONTADOR = 0
    
    #CICLO PARA ITERACIONES
    for ENTRADA in X:

        YR = []
        for PESO in PESOS :
            YR.append((ENTRADA @ PESO)-UMBRAL[IT])


        SALIDA = []
        print("YR",YR,"\n")

        if funcion == '0':
            SALIDA = []   
            for i in range(YD.ndim):
                for j in range(len(ENTRADA)):
                    suma_funcion_soma = (ENTRADA[j] * PESOS[i][j]) - UMBRAL[i]
                    SALIDA.append(suma_funcion_soma)

        elif funcion == '1':
            salida_soma = FuncionSoma(ENTRADA)
            SALIDA = []
            for n in range(len(salida_soma)):
                SALIDA.append(1 / (1 + np.exp(-salida_soma[n])))

        elif funcion == '2':
            salida_soma = FuncionSoma(ENTRADA)
            SALIDA = salida_soma

        ERROR_LINEAL = np.subtract(YD[CONTADOR], SALIDA)

        ERROR_PATRON.append(abs(ERROR_LINEAL).sum()/len(ERROR_LINEAL))

        CONTADOR += 1

        for j in range(len(PESOS)) :
            for i in range(len(PESOS[0])) :
                PESOS[j][i] += RATA * ERROR_LINEAL[j] * ENTRADA[i]

        for j in range(len(UMBRAL)) :
            UMBRAL[j] += RATA*ERROR_LINEAL[j]

    ERROR_RMS = np.abs(ERROR_PATRON).sum()/len(ERROR_PATRON)
    ITERATE += 1

    if ((ITERATE > NUMERO_ITERACIONES- 1) or (ERROR_RMS <= ERROR)) :
        break

if (ERROR_RMS <= ERROR):
        np.savetxt('Data/pesos',PESOS, delimiter =' ')
        np.savetxt('Data/umbral',UMBRAL, delimiter =' ')
else:
    print('Fail')

    def FuncionSoma(self, patron):
        
        return salida

    def FuncionEscalon(self, salida_resultante):
        salida = []
        for escalon in salida_resultante:
            salida_resultante_new = 1 if escalon >= 0 else 0
            salida.append(salida_resultante_new)
        return salida

    def FuncionSigmoide(self, salida_soma):
        salida_resultante = []
        for n in range(len(salida_soma)):
            salida_resultante.append(1 / (1 + np.exp(-salida_soma[n])))
        return salida_resultante

    def FuncionLineal(self, salida_soma):
        salida_resultante = salida_soma
        return salida_resultante


