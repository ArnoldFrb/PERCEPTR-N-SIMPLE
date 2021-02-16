import numpy as np

X = np.array([[1,0,1], [0,1,1], [1,1,0]])

YD = np.array([[1,0], [0,1], [1,1]])

PESOS = np.array([[0.1,-0.5,-0.9], [0.6,0.2,-0.3]])

UMBRAL = np.array([[0.5], [-0.8]])

M = 3
N = 2
P = 3

RA = 1
ER = 0.1
NI = 1000

for ENTRADA in X:
    SALIDA = []
    for PESO in PESOS:
        print(ENTRADA * PESO, "=", ENTRADA @ PESO)
        SALIDA.append(ENTRADA @ PESO)

    YR = SALIDA
    SALIDA = []

    for ESCALON in YR:
        if ESCALON >= 0:
            SALIDA.append(1)
        else:
            SALIDA.append(0)

    print(SALIDA)
    print("******")
    '''for YDa in YD:
        print(YDa)
        print(np.subtract(YDa, YR))
    '''
    print("-----")