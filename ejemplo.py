from subprocess import run
from random import randrange

if __name__=='__main__':
    run('cls', shell=True)

    n1 = int(input('Dame n1 '))
    n2 = int(input('Dame n2 '))

    if n1==n2:
        L1 = []
        for i in range(n1):
            L1.append( randrange(100) )
        print()

        L2 = []
        for i in range(n2):
            L2.append( randrange(100) )
        print()

        n3 = n1
        L3 = []
        for i in range(n3):
            L3.append( L1[i] + L2[i] )

        print(f'L1={L1}')
        print(f'L2={L2}')
        print(f'L3={L3}')
        print()

        for i in range(n3):
            print(f'[{i}]\t{L1[i]} + {L2[i]}\t= {L3[i]}')

    else:
        print("Error! No pueden sumarse...")
