import numpy as np

X = np.array([[1,0,1], [0,1,1], [1,1,0]])
YD = np.array([[1,0], [0,1], [1,1]])
PESOS = np.array([[0.1,-0.5,-0.9], [0.6,0.2,-0.3]])
UMBRAL = np.array([0.5, -0.8])

ERROR_LINEAL = []

M = 3       #ENTREDAS
N = 2       #SALIDAS
P = 3       #PATRONES

RA = 1      #RATA DE APRENDIZAJE
ER = 0.1    #ERROR LINEAL
NI = 1000   #NUMERO DE ITERACIONES

ITERATE = 0  #ITERACION INICIAL
while True:

    ERROR_PATRON = []   #ERROR PATRON
    cont = 0

    print("---------------------------")
    print("ITERACION: ",ITERATE+1)
    print("---------------------------")
    
    #CICLO PARA ITERACIONES
    for ENTRADA in X:
        print("PATRON: ",cont+1,"\n")
        IT = 0
        YR = []
        for PESO in PESOS :
            YR.append((ENTRADA @ PESO)-UMBRAL[IT])
            IT += 1

        print("PATRON PRESENTADO",ENTRADA,"\n")

        SALIDA = []
        print("YR",YR,"\n")

        for ESCALON in YR:
            if ESCALON >= 0:
                SALIDA.append(1)
            else:
                SALIDA.append(0)

        print("SALIDA DEL PATRON",SALIDA,"\n")

        ERROR_LINEAL = np.subtract(YD[cont], SALIDA)
        print("ERROR_LINEAL",ERROR_LINEAL,"\n")

        ERROR_PATRON.append(abs(ERROR_LINEAL).sum()/len(ERROR_LINEAL))
        print("ERROR_PATRON",ERROR_PATRON,"\n")

        cont += 1

        for j in range(len(PESOS)) :
            for i in range(len(PESOS[0])) :
                PESOS[j][i] += RA * ERROR_LINEAL[j] * ENTRADA[i]

        for j in range(len(UMBRAL)) :
            UMBRAL[j] += RA*ERROR_LINEAL[j]

        print("PESOS",PESOS,"\n")
        print("UMBRAL",UMBRAL,"\n")
        print("---------------------------")

    ERROR_RMS = np.abs(ERROR_PATRON).sum()/len(ERROR_PATRON)
    ITERATE += 1

    print("---------------------------")
    print("ERROR DE LOS PATRONES",ERROR_PATRON,"\n")
    print("ERROR DE LA ITERACION",ERROR_RMS,"\n")

    if ((ITERATE > NI-1) or (ERROR_RMS <= ER)) :
        break