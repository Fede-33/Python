# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

num = None
divisores = 0

while num == None:
    try:
        num = int(input('Ingrese número entero: '))
    except ValueError:
        print('Incorrecto.\n')

for i in range(1, abs(num+1)):
    if num % i == 0:
        divisores = divisores + 1
    if divisores == 3:
        print(f'El número {num} no es primo.')
        exit()    
print(f'El número {num} es primo.')