from os import system

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

if __name__== '__main__':
    system('cls')

    m = int(input('Cuantas filas? '))
    n = int(input('Cuantas columnas? '))

    M = generaMatrizCeros(m, n)
    print(M)
    muestraMatriz(M)