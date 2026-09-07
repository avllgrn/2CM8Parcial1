from subprocess import run
from random import randrange

if __name__=='__main__':
    run('cls', shell=True)

    m = 5
    n = 10

    for i in range( m ):
        for j in range( n ):
            print(f'[{i}][{j}]', end='\t')

        print('\n')
