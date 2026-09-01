from subprocess import run
from random import randrange

def generaVectorAleatorio(n):
    V = []
    for i in range(n):
        V.append( randrange(100)/10 )
    return V

def calculaPromedios(A, B, C):
    P = []
    for i in range(n):
        P.append( (A[i] + B[i] + C[i])/3 )
    return P

def muestraCalificaciones(W, X, Y, Z):
    n = len(W)

    print(f'Alumno\t', end='')
    for i in range(3):
        print(f'P{i+1}\t', end='')
    print('Promedio\n')

    for i in range(n):
        print(f'{i+1}\t{W[i]}\t{X[i]}\t{Y[i]}\t{Z[i]}\t')

def buscaMayorMenor(P):
    n = len(P)

    mayor = P[0]
    menor = P[0]
    for i in range(n):
        if P[i]>mayor:
            mayor = P[i]

        if P[i]<menor:
            menor = P[i]

    return mayor, menor

if __name__=='__main__':
    run('cls', shell=True)

    n = int(input('¿Cuántos alumnos? '))

    p1 = generaVectorAleatorio(n)
    p2 = generaVectorAleatorio(n)
    p3 = generaVectorAleatorio(n)

    prom = calculaPromedios(p1, p2, p3)

    muestraCalificaciones(p1, p2, p3, prom)

    esto = buscaMayorMenor(prom)
    print(type(esto))

    print()
    print(f'El promedio más alto es {esto[0]}.')
    print(f'El promedio más bajo es {esto[1]}.')
    print()
    