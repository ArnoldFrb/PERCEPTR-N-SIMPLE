import numpy as np

X = np.array([[1,0,1], [0,1,1], [1,1,0]])               #MATRIZ ENTRADAS

YD = np.array([[1,0], [0,1], [1,1]])                    #MATRIZ SALIDAS

PESOS = np.array([[0.1,-0.5,-0.9], [0.6,0.2,-0.3]])     #MATRIZ PESOS

UMBRAL = np.array([0.5, -0.8])                          #MATRIZ UMBRAL

M = 3       #ENTREDAS
N = 2       #SALIDAS
P = 3       #PATRONES

RA = 1      #RATA DE APRENDIZAJE
ER = 0.1    #ERROR LINEAL
NI = 1000   #NUMERO DE ITERACIONES

IT = 0      #ITERACION INICIAL

print()
print("---ENTRENAMIENTO---")
print()
#CICLO PARA ITERACIONES
while True:

    EP = []             #ERROR PATRON

    print("---------------------------")
    print("ITERACION: ", IT+1)
    print("---------------------------")

    #OBTENER PATRON DE ENTRASDAS
    for IP in range(P):
        XP = []         #PATRON PRESENTADO
        print("PATRON: ", IP+1)
        print()
        for JP in range(M):
            XP.append(X[IP][JP])
        print("PATRON PRESENTADO")
        print(XP)
        print()

        YDP = []         #PATRON PRESENTADO
        for JP in range(N):
            YDP.append(YD[IP][JP])
        print("SALIDA DEL PATRON")
        print(YDP)
        print()

        #METODO PARA OBTENER LA FUNCION SOMA
        print("FUNCION SOMA")
        SL = []         #SALIDA DE LA FUNCION SOMA
        for IS in range(N):
            SLD = 0     #SUMATORIA DE LA FUNCION SOMA
            for JS in range(M):
                SLD = SLD + (XP[JS] * PESOS[IS][JS])
            SL.append(SLD - UMBRAL[IS])
        print(SL)
        print()

        #METODO PARA OBTENER LA FUNCION ESCALON
        print("FUNCION ESCALON")
        YR = []         #SALIDA DE LA FUNCION ESCALON
        for IEC in range(N):
            if SL[IEC] >= 0:
                YR.append(1)
            else:
                YR.append(0)
        print(YR)
        print()

        #METODO PARA OBTENER EL ERROR LINEAL
        print("ERROR LINEAL")
        EL = []          #ERROR LINEAL
        for IEL in range(N):
            EL.append(YDP[IEL] - YR[IEL])
        print(EL)
        print()
        
        #METODO PARA OBTENER EL ERROR DEL PATRON
        print("ERROR PATRON")
        EP.append((np.abs(EL).sum()) / N)
        print((np.abs(EL).sum()) / N)
        print()

        #METODO PARA ACTUALIZAR PESOS
        print("PESOS ACTUALIZADOS")
        for IPS in range(N):
            for JPS in range(M):
                PESOS[IPS][JPS] = PESOS[IPS][JPS] + (RA * EL[IPS] * XP[JPS])
        print(PESOS)
        print()

        #METODO PARA ACTUALIZAR UMBRALES
        print("UMBRALES ACTUALIZADOS")
        for IU in range(N):
            UMBRAL[IU] = UMBRAL[IU] + (RA * EL[IU] * 1)       
        print(UMBRAL)
        print()
        print("---------------------------")
        
    print("---------------------------")
    print("ERROR DE LOS PATRONES")
    print(EP)
    print()
    #METODO PARA OBTENER EL ERROR DE LA ITERACION
    print("ERROR DE LA ITERACION")
    ERMS = (np.sum(EP)) / P
    print(ERMS)
    print()

    IT+=1
    if((IT > NI-1) or (ERMS <= ER)):
        break

print("NUMERO DE ITERACIONES REALIZADAS: ", IT)
print()
