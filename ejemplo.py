from subprocess import run

if __name__=='__main__':
    run('cls', shell=True)
    M = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

    print(M, type(M))
    print()

    print(M[0], type(M[0]))
    print(M[1], type(M[1]))
    print(M[2], type(M[2]))
    print()

    print(M[0][0], type(M[0][0]))
    print(M[0][1], type(M[0][1]))
    print(M[0][2], type(M[0][2]))
    print()

    print(M[1][0], type(M[1][0]))
    print(M[1][1], type(M[1][1]))
    print(M[1][2], type(M[1][2]))
    print()

    print(M[2][0], type(M[2][0]))
    print(M[2][1], type(M[2][1]))
    print(M[2][2], type(M[2][2]))
    print()


    print(M[0][0], end='\t')
    print(M[0][1], end='\t')
    print(M[0][2], end='\t')
    print()

    print(M[1][0], end='\t')
    print(M[1][1], end='\t')
    print(M[1][2], end='\t')
    print()

    print(M[2][0], end='\t')
    print(M[2][1], end='\t')
    print(M[2][2], end='\t')
    print()

    print('\n\n')

    for i in range(3):
        for j in range(3):
            print(M[i][j], end='\t')
        print()
