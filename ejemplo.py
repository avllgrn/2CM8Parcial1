from os import system
from random import randrange

def generaVector(n):
    V = []
    for i in range(n):
        V.append(randrange(100))
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

if __name__== '__main__':
    system('cls')

    n = int(input('Cuántos datos? '))
    V = generaVector(n)
    print('V')
    muestraVector(V)
    print()

    pMenor = menorEnVector(V)
    menor = V[pMenor]
    pMayor = mayorEnVector(V)
    mayor = V[pMayor]

    print(f'El valor menor es {menor} y está en [{pMenor}]')
    print(f'El valor mayor es {mayor} y está en [{pMayor}]')
