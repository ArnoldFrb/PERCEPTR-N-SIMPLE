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

for n in range(YD.ndim):
    fila = []
    for M in range(len(X[0])):
        fila.append(round(rn.uniform(-1, 1), 2))
    PESOS.append(fila)


for n in range(YD.ndim):
    UMBRAL.append(round(rn.uniform(-1, 1), 2))

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

        for ESCALON in YR:
            if ESCALON >= 0:
                SALIDA.append(1)
            else:
                SALIDA.append(0)

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


