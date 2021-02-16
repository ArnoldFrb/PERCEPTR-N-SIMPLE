import numpy as np

#MATRICES

#ENTRADAS
X = np.array([[1,0,1], [0,1,1], [1,1,0]])

#SALIDAS
YD = np.array([[1,0], [0,1], [1,1]])

#CONFIGURACION DE LA NEURONA
M = 3
N = 2
P = 3

RA = 1
ER = 0.1
NI = 1000

#APRENDIZAJE
for SALIDAS in np.nditer(X, order='F'):
    print(SALIDAS, end=' ')


#print("X = ", X)
#print("")
#print("Y = ", YD)