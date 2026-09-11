from subprocess import run
from random import randrange

def generaMatriz(m,n):
    # Se genera una matriz de m filas por n columnas
    M = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append( 0 ) # Llena de ceros
        M.append( fila )
    return M

def muestraMatriz(X):
    m = len(X)
    n = len(X[0])
    # Se muestra una matriz de 
    for i in range(m): # m filas por 
        for j in range(n): # n columnas
            print(X[i][j], end='\t')
        print()

def rellenaConContador(X):
    m = len(X)
    n = len(X[0])
    cont = 1
    for i in range(m):
        for j in range(n):
            X[i][j] = cont
            cont += 1

def rellenaIdentidad(X):
    n = len(X)
    for i in range(n):
        for j in range(n):
            if i==j:
                X[i][j] = 1
            else:
                X[i][j] = 0

def generaMatrizAleatorios(m,n):
    # Se genera una matriz de m filas por n columnas
    M = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append( randrange(100) ) # Llena de ceros
        M.append( fila )
    return M

def copiaMatriz(X):
    m = len(X)
    n = len(X[0])

    Copia = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append(X[i][j])
        Copia.append( fila )
    return Copia

def rellenaTranspuesta(MT, M):
    m = len(M)
    n = len(M[0])

    for i in range(m):
        for j in range(n):
            MT[j][i] = M[i][j]

if __name__=='__main__':
    run('cls', shell=True)

    print('Genera Matriz con ceros y después cambiarlos por un contador\n\n')
    m = int(input('Filas? '))
    n = int(input('Columnas? '))

    # Genera matriz
    M = generaMatriz(m,n)
    muestraMatriz(M)
    print()

    # Rellenala con un contador
    rellenaConContador(M)
    muestraMatriz(M)
    print()
    input('Presiona Enter para continuar...')
    run('cls', shell=True)


    print('Genera Matriz con ceros y después cambiarla por Identidad\n\n')
    n = int(input('Filas y Columnas? '))
    # Genera matriz
    I = generaMatriz(n,n)
    muestraMatriz(I)
    print()

    rellenaIdentidad(I)
    muestraMatriz(I)
    print()
    input('Presiona Enter para continuar...')
    run('cls', shell=True)


    print('Copiar una Matriz\n\n')
    m = int(input('Filas? '))
    n = int(input('Columnas? '))

    # Genera matriz
    Original = generaMatrizAleatorios(m,n)
    muestraMatriz(Original)
    print()

    C = copiaMatriz(Original)
    muestraMatriz(C)
    print()
    input('Presiona Enter para continuar...')
    run('cls', shell=True)


    print('Genera Matriz Transpuesta\n\n')
    m = int(input('Filas? '))
    n = int(input('Columnas? '))

    # Genera matriz
    Matriz = generaMatrizAleatorios(m,n)
    muestraMatriz(Matriz)
    print()

    mT = n
    nT = m
    Transpuesta = generaMatriz(mT, nT)
    rellenaTranspuesta(Transpuesta, Matriz)
    muestraMatriz(Transpuesta)
    print()

