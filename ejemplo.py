from subprocess import run
from random import randrange

def muestraMatriz(X):
    m = len(X)
    n = len(X[0])
    for i in range(m):
        for j in range(n):
            print(X[i][j], end='\t')
        print()

def generaMatrizCeros(m, n):
    M = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append( 0 )
        M.append(fila)
    return M

def generaMatrizAleatorios(m, n):
    M = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append( randrange(100) )
        M.append(fila)
    return M

def generaMatrizConteo(m, n):
    M = []
    cont = 1
    for i in range(m):
        
        fila = []
        for j in range(n):
            fila.append( cont )
            cont+=1
        M.append(fila)
    return M

def generaMatrizContFila(m, n):
    M = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append( i )
        M.append(fila)
    return M

def generaMatrizContColumna(m, n):
    M = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append( j )
        M.append(fila)
    return M

if __name__=='__main__':
    run('cls', shell=True)

    filas = int(input('Cuántas filas? '))
    columnas = int(input('Cuántas columas? '))

    M1 = generaMatrizCeros(filas, columnas)
    muestraMatriz(M1)
    print()

    M2 = generaMatrizAleatorios(filas, columnas)
    muestraMatriz(M2)
    print()

    M3 = generaMatrizConteo(filas, columnas)
    muestraMatriz(M3)
    print()

    M4 = generaMatrizContFila(filas, columnas)
    muestraMatriz(M4)
    print()

    M5 = generaMatrizContColumna(filas, columnas)
    muestraMatriz(M5)
    print()
