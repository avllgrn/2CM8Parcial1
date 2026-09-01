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
    posMay = 0
    menor = P[0]
    posMen = 0
    for i in range(n):
        if P[i]>mayor:
            mayor = P[i]
            posMay = i

        if P[i]<menor:
            menor = P[i]
            posMen = i

    return (posMay, mayor), (posMen, menor)

def cuentaAprobadosReprobados(P):
    n = len(P)
    aprobados=0
    reprobados=0
    for i in range(n):
        if P[i]>=6:
            aprobados += 1
        else:
            reprobados += 1

    return aprobados, reprobados

if __name__=='__main__':
    run('cls', shell=True)

    n = int(input('¿Cuántos alumnos? '))

    p1 = generaVectorAleatorio(n)
    p2 = generaVectorAleatorio(n)
    p3 = generaVectorAleatorio(n)

    prom = calculaPromedios(p1, p2, p3)

    muestraCalificaciones(p1, p2, p3, prom)

    esto = buscaMayorMenor(prom)

    print()
    print(f'esto es {type(esto)} y contiene {esto}')

    mejorAlumno = esto[0]
    peorAlumno = esto[1]
    print('El mejor alumno es', mejorAlumno[0]+1, 'su promedio es', mejorAlumno[1],'.')
    print('El peor alumno es', peorAlumno[0]+1, 'su promedio es', peorAlumno[1],'.')
    print()

    estoOtro = cuentaAprobadosReprobados(prom)
    print(f'estoOtro es {type(estoOtro)} y contiene {estoOtro}')

    print('Aprobaron: ', estoOtro[0])
    print('Reprobaron: ', estoOtro[1])
    print()
    