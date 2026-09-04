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

def intercala(X, Y):
    Z = []
    n1 = len(X)
    n2 = len(Y)

    i=0
    j=0
    while i<n1 and i<n2:
        Z.append(X[i])
        Z.append(Y[j])
        i+=1
        j+=1

    while i<n1:
        Z.append(X[i])
        i+=1

    while j<n2:
        Z.append(Y[j])
        j+=1

    return Z

if __name__=='__main__':
    run('cls', shell=True)

    n1 = int(input('Dame n1 '))
    n2 = int(input('Dame n2 '))

    V1 = generaVectorAleatorio(n1)
    V2 = generaVectorAleatorio(n2)
    V3 = intercala(V1,V2)

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

