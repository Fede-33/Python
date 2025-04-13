import random

n = random.randint(1,100)

print('ADIVINAR EL NÚMERO')

for i in range(10,0,-1):
    print(f'\nAún le quedan {i} intentos.')
    var = int(input('Adivine el número entre 1 y 100:  '))
    if var == n:
        print('\nCORRECTO GANASTE\n')
        break
    elif var > n:
        print('\nIncorrecto, demasiado alto.\n')
    else:
        print('\nIncorrecto, demasiado bajo.\n')

if var != n:
    print('PERDISTE')