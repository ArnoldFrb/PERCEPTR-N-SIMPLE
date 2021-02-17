import numpy as np

X = np.array([[1,0,1], [0,1,1], [1,1,0]])               #MATRIZ ENTRADAS

YD = np.array([[1,0], [0,1], [1,1]])                    #MATRIZ SALIDAS

PESOS = np.array([[0.1,-0.5,-0.9], [0.6,0.2,-0.3]])     #MATRIZ PESOS

UMBRAL = np.array([[0.5], [-0.8]])                      ##MATRIZ UMBRAL

M = 3       #ENTREDAS
N = 2       #SALIDAS
P = 3       #PATRONES

RA = 1      #RATA DE APRENDIZAJE
ER = 0.1    #ERROR LINEAL
NI = 1000   #NUMERO DE ITERACIONES

IT = 0      #ITERACION INICIAL

print()

#CICLO PARA ITERACIONES
while True:

    print("---ENTRENAMIENTO---")
    print()

    #OBTENER PATRON DE ENTRASDAS
    for IP in range(P):
        XP = []     #PATRON PRESENTADO
        for JP in range(M):
            XP.append(X[IP][JP])
        print(XP)

        print()
        print("FUNCION SOMA")
        SL = []
        for IS in range(N):
            SLD = 0
            for JS in range(M):
                SLD = SLD + (XP[JS] * PESOS[IS][JS])
            SL.append(SLD - UMBRAL[IS])
        print(SL)

        print()
        print()
        print("---------------------------")

    IT+=1
    if(IT != 0):
        break

print()
print("NUMERO DE ITERACIONES REALIZADAS", IT)
print()
