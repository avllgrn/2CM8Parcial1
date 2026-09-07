from subprocess import run
from random import randrange

if __name__=='__main__':
    run('cls', shell=True)

    m = 5
    n = 100000

    for i in range( m ):
        for j in range( n ):
            print(f'i={i} j={j}')
