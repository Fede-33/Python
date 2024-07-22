# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

nums = []

for i in range (6):
    nums.append(int(input('Ingrese número ganador: ')))

nums.sort()
print(f'Los números ganadores son: {nums}' )
