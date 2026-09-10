from subprocess import run

if __name__=='__main__':
    run('cls', shell=True)

    m = int(input('Filas? '))
    n = int(input('Columnas? '))

    # Se genera una matriz de m filas por n columnas
    M = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append( 0 ) # Llena de ceros
        M.append( fila )

    print(M)
    print()

    # Se muestra una matriz de 
    for i in range(m): # m filas por 
        for j in range(n): # n columnas
            print(M[i][j], end='\t')
        print()
