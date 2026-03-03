from os import system
from random import randrange

def generaMatrizCeros(m, n):
    M = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append( 0 )
        M.append( fila )
    return M

def muestraMatriz(M):
    m = len(M)
    n = len( M[0] )
    for i in range(m):
        for j in range(n):
            print(M[i][j], end='\t')
        print()

def leeMatriz(m, n):
    M = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append( int(input(f'Ingresa [{i}][{j}] ')) )
        M.append( fila )
    return M

def generaMatrizAleatorios(m, n, inf, sup):
    M = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append( randrange(inf, sup) )
        M.append( fila )
    return M

def generaMatrizIdentidad(n):
    M = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i==j:
                fila.append( 1 )
            else:
                fila.append( 0 )
        M.append( fila )
    return M

def generaMatrizConteo(m, n, ini, inc):
    M = []
    contador = ini
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append( contador )
            contador += inc
        M.append( fila )
        
    return M

def generaMatrizConteoIzqDerArrAba(m, n, ini, inc):
    M = generaMatrizCeros(m,n)

    contador = ini
    for i in range(m):
        for j in range(n):
            M[i][j] = contador
            contador += inc
        
    return M

def generaMatrizConteoArrAbaIzqDer(m, n, ini, inc):
    M = generaMatrizCeros(m,n)

    contador = ini
    for j in range(n):
        for i in range(m):
            M[i][j] = contador
            contador += inc
        
    return M

def generaMatrizConteoDerIzqArrAba(m, n, ini, inc):
    M = generaMatrizCeros(m,n)

    contador = ini
    for i in range(m):
        for j in range(n-1, -1, -1):
            M[i][j] = contador
            contador += inc
        
    return M

def generaMatrizConteoArrAbaDerIzq(m, n, ini, inc):
    M = generaMatrizCeros(m,n)

    contador = ini
    for j in range(n-1, -1, -1):
        for i in range(m):
            M[i][j] = contador
            contador += inc

    return M

def posiciones(m,n):
    for i in range(m):
        for j in range(n):
            print(f'[{i}][{j}]', end='\t')
        print()

def triangularInferior(n):
    M = generaMatrizCeros(n,n)
    for i in range(n):
        for j in range(n):
            if i>=j:
                M[i][j] = randrange(100)
    return M

def triangularSuperior(n):
    M = generaMatrizCeros(n,n)
    for i in range(n):
        for j in range(n):
            if i<=j:
                M[i][j] = randrange(100)
    return M
    
def triangularInferior(n):
    M = generaMatrizCeros(n,n)
    for i in range(n):
        for j in range(n):
            if i>=j:
                M[i][j] = randrange(100)
    return M

def triangularSuperior(n):
    M = generaMatrizCeros(n,n)
    for i in range(n):
        for j in range(n):
            if i<=j:
                M[i][j] = randrange(100)
    return M
    
def generaTriangularInferiorIzqDerArrAba(n, ini, inc):
    M = generaMatrizCeros(n,n)
    contador = ini
    for i in range(n):
        for j in range(n):
            if i>=j:
                M[i][j] = contador
                contador += inc
    return M

def generaTriangularSuperiorIzqDerArrAba(n, ini, inc):
    M = generaMatrizCeros(n,n)
    contador = ini
    for i in range(n):
        for j in range(n):
            if i<=j:
                M[i][j] = contador
                contador += inc
    return M

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

def copiaMatriz(M):
    m = len(M)
    n = len(M[0])
    Copia = generaMatrizCeros(m, n)
    for i in range(m):
        for j in range(n):
            Copia[i][j] = M[i][j]
    return Copia

def generaTranspuesta(M):
    mT = len(M[0])
    nT = len(M)
    MT = generaMatrizCeros(mT, nT)
    for i in range(m):
        for j in range(n):
           MT[j][i] = M[i][j]
    return MT

if __name__== '__main__':
    system('cls')
   
    m = int(input('Cuántas filas? '))
    n = int(input('Cuántas columnas? '))
    M = generaMatrizAleatorios(m,n,0,100)
    MT = generaTranspuesta(M)

    print('\nM')
    muestraMatriz(M)
    print('\nMT')
    muestraMatriz(MT)
