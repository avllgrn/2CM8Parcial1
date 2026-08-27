from subprocess import run

if __name__=='__main__':
    run('cls', shell=True)

    # Collecciones ordenadas
    # Collecciones desordenadas
    # Collecciones mutables
    # Collecciones inmutables

    lista = list()
    print(lista, type(lista), len(lista))

    lista = []
    print(lista, type(lista), len(lista))

    lista.append(51)
    print(lista, type(lista), len(lista))

    lista.append(14)
    print(lista, type(lista), len(lista))

    lista.append(38)
    print(lista, type(lista), len(lista))

    lista.append(29)
    print(lista, type(lista), len(lista))

    lista.append(71)
    print(lista, type(lista), len(lista))
    print('\n\n')

    print(f'Salió {lista.pop()}')
    print(lista, type(lista), len(lista))

    print(f'Salió {lista.pop()}')
    print(lista, type(lista), len(lista))

    print(f'Salió {lista.pop()}')
    print(lista, type(lista), len(lista))

    print(f'Salió {lista.pop()}')
    print(lista, type(lista), len(lista))

    print(f'Salió {lista.pop()}')
    print(lista, type(lista), len(lista))

    # Nunca pop a lista vacía
    # print('\n\n')
    # print(f'Salió {lista.pop()}')
    # print(lista, type(lista), len(lista))
