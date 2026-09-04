from subprocess import run
from random import randrange

def generaVectorAleatorio(n):
    Original = []
    for i in range(n):
        Original.append( randrange(100)/10 )
    return Original

def muestraVector(X):
    n = len(X)
    for i in range(n):
        print(f'[{i}] = {X[i]}')

def copiaDe(X):
    Y = []
    n = len(X)
    for i in range(n):
        Y.append(X[i])
    return Y

if __name__=='__main__':
    run('cls', shell=True)

    n = int(input('Dame n '))

    Original = generaVectorAleatorio(n)
    print(Original)

    Copia = copiaDe(Original)
    print(Copia)
    print('\nOriginal')
    muestraVector(Original)
    print('\nCopia')
    muestraVector(Copia)

    Copia[0] = 100
    print()
    print(Original)
    print(Copia)
    print()
    print('\nOriginal')
    muestraVector(Original)
    print('\nCopia')
    muestraVector(Copia)
