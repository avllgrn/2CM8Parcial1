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

def menorEnMatriz(M):
    m = len(M)
    n = len(M[0])
    menor = M[0][0]
    filaMenor = 0
    columnaMenor = 0
    for i in range(m):
        for j in range(n):
            if M[i][j]<menor:
                menor=M[i][j]
                filaMenor = i
                columnaMenor = j

    return (filaMenor, columnaMenor)

def mayorEnMatriz(M):
    m = len(M)
    n = len(M[0])
    mayor = M[0][0]
    filaMayor = 0
    columnaMayor = 0
    for i in range(m):
        for j in range(n):
            if M[i][j]>mayor:
                mayor=M[i][j]
                filaMayor = i
                columnaMayor = j

    return (filaMayor, columnaMayor)

def cuentaDatoEnMatriz(x, M):
    m = len(M)
    n = len(M[0])
    veces = 0
    for i in range(m):
        for j in range(n):
            if M[i][j]==x:
                veces += 1

    return veces

def sumaMatrices(M1, M2):
    m1 = len(M1)
    n1 = len(M1[0])
    m2 = len(M2)
    if m1==m2 or n1==n2:
        m3 = m1 = m2
        n3 = n1 = n2
        S = generaMatrizCeros(m3, n3)
        for i in range(m3):
            for j in range(n3):
                S[i][j] = M1[i][j] + M2[i][j]
    else:
        S = []
    
    return S

def restaMatrices(M1, M2):
    m1 = len(M1)
    n1 = len(M1[0])
    m2 = len(M2)
    if m1==m2 or n1==n2:
        m3 = m1 = m2
        n3 = n1 = n2
        R = generaMatrizCeros(m3, n3)
        for i in range(m3):
            for j in range(n3):
                R[i][j] = M1[i][j] - M2[i][j]
    else:
        R = []
    
    return R

def sumaDatosEnMatriz(M):
    m = len(M)
    n = len(M[0])
    suma = 0
    for i in range(m):
        for j in range(n):
            suma += M[i][j]

    return suma

def promediaDatosEnMatriz(M):
    m = len(M)
    n = len(M[0])
    suma = 0
    for i in range(m):
        for j in range(n):
            suma += M[i][j]

    return suma/(m*n)

if __name__== '__main__':
    system('cls')
   
    m = int(input('Cuántas filas de matriz? '))
    n = int(input('Cuántas columnas de matriz? '))
    M = generaMatrizAleatorios(m,n,1,100)
    print('\nM')
    muestraMatriz(M)
    print()

    s = sumaDatosEnMatriz(M)
    p = promediaDatosEnMatriz(M)

    print(f'La suma de los datos es {s}')
    print(f'El promedio de los datos es {p}')
