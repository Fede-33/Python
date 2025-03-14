# Construir un programa para realizar las siguientes operaciones con dos números proporcionados por el usuario:

n_1 = int(input('Ingrese un número entero: '))
n_2 = int(input('Ingrese un número entero: '))

    #1 Comprobar si uno de los dos números es divisible por el otro. Un número es divisible por otro cuando el resto de la división entera es cero.
    
if (n_1 % n_2 == 0) or (n_2 % n_1 == 0):
    print('Son divisibles')
else:
    print('No son divisibles')
    #2 Calcular su Máximo Común Divisor.
    
divisores = []
for i in range(1, min(n_1 ,n_2)+1):
    if n_1 % i == 0 and n_2 % i == 0:
        divisores.append(i)
    
if divisores == []:
    print(f'{n_1} y {n_2} no tienen divisores en común.')
else:
    print(f'El Máximo Común Divisor entre {n_1} y {n_2} es {max(divisores)}')

    #3 Calcular su Mínimo Común Múltiplo.

multiplos = []    

for i in range(1, min(n_1, n_2)+1):
    if (i * max(n_1 , n_2)) % (min(n_1, n_2)) == 0:
        multiplos.append(i * max(n_1 , n_2))

print(f'El Mínimo Común Múltiplo entre {n_1} y {n_2} es {min(multiplos)}')

    #4 Cada una de las operaciones deben estar separadas en funciones que tengan como parámetros los 2 números y devuelvan el resultado adecuado.


