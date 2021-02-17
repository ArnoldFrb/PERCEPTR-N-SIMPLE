import numpy as np

X = np.array([[1,0,1], [0,1,1], [1,1,0]])
YD = np.array([[1,0], [0,1], [1,1]])
PESOS = np.array([[0.1,-0.5,-0.9], [0.6,0.2,-0.3]])
UMBRAL = np.array([[0.5], [-0.8]])
ERROR_LINEAL = []

M = 3
N = 2
P = 3
RA = 1
ER = 0.1
NI = 1000
cont = 0

for ENTRADA in X:
    YR = []

    for PESO in PESOS:
        print(ENTRADA * PESO, "=", ENTRADA @ PESO)
        YR.append(ENTRADA @ PESO)

    SALIDA = []
    print("----------------------------------------")
    print("YR = ",YR)

    for ESCALON in YR:
        if ESCALON >= 0:
            SALIDA.append(1)
        else:
            SALIDA.append(0)

    print("Salida = ",SALIDA)
    print("----------------------------------------")
    np.subtract(YD[cont], YR)
    
    cont+=1
    print("////////////////////////////////////////")