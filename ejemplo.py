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

def unir(X, Y):
    Z = []
    n1 = len(X)
    n2 = len(Y)

    for i in range(n1):
        Z.append(X[i])

    for i in range(n2):
        Z.append(Y[i])

    return Z

if __name__=='__main__':
    run('cls', shell=True)

    n1 = int(input('Dame n1 '))
    n2 = int(input('Dame n2 '))

    V1 = generaVectorAleatorio(n1)
    V2 = generaVectorAleatorio(n2)
    V3 = unir(V1,V2)

    print()
    print(V1)
    print(V2)
    print(V3)
    print()
    print('\nV1')
    muestraVector(V1)
    print('\nV2')
    muestraVector(V2)
    print('\nV3')
    muestraVector(V3)

