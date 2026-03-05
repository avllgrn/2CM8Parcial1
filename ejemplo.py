from os import system
from random import randrange

def generaVector(n):
    V = []
    for i in range(n):
        V.append(randrange(10))
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

def menorEnVector(V):
    n = len(V)
    menor = V[0]
    posicionMenor = 0
    for i in range(n):
        if V[i]<menor:
            menor=V[i]
            posicionMenor = i
    return posicionMenor

def mayorEnVector(V):
    n = len(V)
    mayor = V[0]
    posicionMayor = 0
    for i in range(n):
        if V[i]>mayor:
            mayor=V[i]
            posicionMayor = i
    return posicionMayor

def sumaDatosEnVector(V):
    n = len(V)
    suma = 0
    for i in range(n):
        suma += V[i]
    return suma

def promediaDatosEnVector(V):
    n = len(V)
    suma = 0
    for i in range(n):
        suma += V[i]
    return suma/n

def cuentaDatoEnVector(x, V):
    n = len(V)
    veces = 0
    for i in range(n):
        if V[i]==x:
            veces += 1
    return veces

def sumaVectores(A, B):
    nA = len(A)
    nB = len(B)
    C = []
    if nA==nB:
        nC = nA = nB
        for i in range(nC):
            C.append(A[i] + B[i])
    return C

def restaVectores(A, B):
    nA = len(A)
    nB = len(B)
    C = []
    if nA==nB:
        nC = nA = nB
        for i in range(nC):
            C.append(A[i] - B[i])
    return C

def buscaCaracter(caracter, cadena):
    n = len(cadena)
    for i in range(n):
        if cadena[i]==caracter:
            return True
    return False

def cuentaCaracter(caracter, cadena):
    n = len(cadena)
    veces = 0
    for i in range(n):
        if cadena[i]==caracter:
            veces += 1
    return veces

def copiaCadena(cadena):
    copia = ''
    n = len(cadena)
    for i in range(n):
        copia = copia + cadena[i]
    return copia

def copiaCadenaInvertida(cadena):
    copia = ''
    n = len(cadena)
    for i in range(n):
        copia = cadena[i] + copia
    return copia

def convierteCadenaEnLista(cadena):
    lista = []
    n = len(cadena)
    for i in range(n):
        lista.append(cadena[i])
    return lista

def convierteCadenaEnListaDeMayusculas(cadena):
    lista = []
    n = len(cadena)
    for i in range(n):
        lista.append(cadena[i].upper())
    return lista

def convierteCadenaEnListaSinEspeciales(cadena:str):
    lista = []
    n = len(cadena)
    for i in range(n):
        if cadena[i].isalnum():
            lista.append(cadena[i])
    return lista

def esCapicua(entero):
    n = len(entero)
    # Se buscan diferencias desde los extremos hacia la mitad de la cadena
    i = 0
    j = n-1
    while i<j:
        if entero[i] != entero[j]:
            return False
        i += 1
        j -= 1

    return True

def esPalindromo(palindromo):
    # Se convierte cadena a lista en mayusculas sin especiales
    lista = []
    nPalindromo = len(palindromo)
    for i in range(nPalindromo):
        if palindromo[i].isalnum():
            lista.append(palindromo[i].upper())

    # Se buscan diferencias desde los extremos hacia la mitad de la lista
    nLista = len(lista)
    i = 0
    j = nLista-1
    while i<j:
        if lista[i] != lista[j]:
            return False
        i += 1
        j -= 1

    return True

if __name__== '__main__':
    system('cls')
    cadenaEntero = input('Ingresa un número entero ')
    if esCapicua(cadenaEntero):
        print(f'{cadenaEntero} ES capicúa')
    else:
        print(f'{cadenaEntero} NO es capicúa')

    input('Presiona una tecla para continuar...')
    system('cls')

    palindromo = input('Ingresa un palíndromo ')
    if esPalindromo(palindromo):
        print(f'{palindromo} ES palíndromo')
    else:
        print(f'{palindromo} NO es palíndromo')

# Ejemplos de capicúas: 1234321 y 11223344332211
# Ejemplo de palíndromo: ¡¡¡Anita!!! ¡¡¡Lava la !"#$%&/()= tina!!!
