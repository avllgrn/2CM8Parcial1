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

def buscaCaracter(caracter, cadena):
    n = len(cadena)
    for i in range(n):
        if cadena[i]==caracter:
            return True
    return False
    
def cuentaCaracter(caracter, cadena):
    n = len(cadena)
    veces = 0
    for i in range(n):
        if cadena[i]==caracter:
            veces += 1
    return veces

if __name__== '__main__':
    system('cls')

    cadena = input('Ingresa una cadena ')
    caracter = input('Qué caracter buscas en tu cadena? ')

    if buscaCaracter(caracter, cadena):
        tantas = cuentaCaracter(caracter, cadena)
        print(f'{caracter} ESTÁ {tantas} veces en tu cadena.')
    else:
        print(f'{caracter} NO está en tu cadena.')
