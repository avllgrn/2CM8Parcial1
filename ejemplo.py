from subprocess import run

if __name__=='__main__':
    run('cls', shell=True)

    lista = [51, -3, 5, 71, 29]
    print(lista, type(lista), len(lista))
    print()

    n = len(lista)
    for i in range(n):
        print( f'lista[{i}] = {lista[i]}' )
    print()

    i=0 
    while i<n:
        print( f'lista[{i}] = {lista[i]}' )
        i += 1
    print()

