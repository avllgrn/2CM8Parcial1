from subprocess import run
from random import randrange

def generaVectorAleatorio(n):
    V = []
    for i in range(n):
        V.append( randrange(100)/10 )
    return V

if __name__=='__main__':
    run('cls', shell=True)

    n = int(input('¿Cuántos alumnos? '))

    p1 = generaVectorAleatorio(n)
    p2 = generaVectorAleatorio(n)
    p3 = generaVectorAleatorio(n)

    prom = []
    for i in range(n):
        prom.append( (p1[i] + p2[i] + p3[i])/3 )

    print(f'Alumno\t', end='')
    for i in range(3):
        print(f'P{i+1}\t', end='')
    print('Promedio\n')

    for i in range(n):
        print(f'{i+1}\t{p1[i]}\t{p2[i]}\t{p3[i]}\t{prom[i]}\t')
