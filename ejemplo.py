from subprocess import run
from random import randrange

def generaVectorAleatorio(n):
    V = []
    for i in range(n):
        V.append( randrange(100) )
    return V

def sumaDosVectores(A, B):
    n = len(A)
    C = []
    for i in range(n):
        C.append( A[i] + B[i] )    
    return C

def muestraVectores(X, Y, Z):
    n = len(X)
    for i in range(n):
        print(f'[{i}]\t{X[i]} + {Y[i]}\t= {Z[i]}')

if __name__=='__main__':
    run('cls', shell=True)

    n1 = int(input('Dame n1 '))
    n2 = int(input('Dame n2 '))

    if n1==n2:
        L1 = generaVectorAleatorio(n1)
        L2 = generaVectorAleatorio(n2)

        L3 = sumaDosVectores(L1, L2)

        muestraVectores(L1, L2, L3)


    else:
        print("Error! No pueden sumarse...")
