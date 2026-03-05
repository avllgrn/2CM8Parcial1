from os import system
from random import randrange

def generaVector(n):
    V = []
    for i in range(n):
        V.append(randrange(10))
    return V

def muestraVector(V):
    n = len(V)
    for i in range(n):
        print(f'[{i}] = {V[i]}')
        
def copiaVector(V):
    Copia = []
    n = len(V)
    for i in range(n):
        Copia.append( V[i] )
    return Copia

def menorEnVector(V):
    n = len(V)
    menor = V[0]
    posicionMenor = 0
    for i in range(n):
        if V[i]<menor:
            menor=V[i]
            posicionMenor = i
    return posicionMenor

def mayorEnVector(V):
    n = len(V)
    mayor = V[0]
    posicionMayor = 0
    for i in range(n):
        if V[i]>mayor:
            mayor=V[i]
            posicionMayor = i
    return posicionMayor

def sumaDatosEnVector(V):
    n = len(V)
    suma = 0
    for i in range(n):
        suma += V[i]
    return suma

def promediaDatosEnVector(V):
    n = len(V)
    suma = 0
    for i in range(n):
        suma += V[i]
    return suma/n

def cuentaDatoEnVector(x, V):
    n = len(V)
    veces = 0
    for i in range(n):
        if V[i]==x:
            veces += 1
    return veces

def sumaVectores(A, B):
    nA = len(A)
    nB = len(B)
    C = []
    if nA==nB:
        nC = nA = nB
        for i in range(nC):
            C.append(A[i] + B[i])
    return C

def restaVectores(A, B):
    nA = len(A)
    nB = len(B)
    C = []
    if nA==nB:
        nC = nA = nB
        for i in range(nC):
            C.append(A[i] - B[i])
    return C

if __name__== '__main__':
    system('cls')

    n1 = int(input('Cuántos datos tiene V1? '))
    n2 = int(input('Cuántos datos tiene V1? '))

    if n1==n2:
        V1 = generaVector(n1)
        V2 = generaVector(n2)
        V3 = sumaVectores(V1, V2)
        V4 = restaVectores(V1, V2)
        print('V1')
        muestraVector(V1)
        print()
        print('V2')
        muestraVector(V2)
        print()
        print('V1+V2')
        muestraVector(V3)
        print()
        print('V1-V2')
        muestraVector(V4)
        print()
    else:
        print('No pueden sumarse ni restarse...')
