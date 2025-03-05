# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo de asteriscos, donde n es el número de filas de altura del triángulo.

n = int(input('Ingrese un número entero: '))

for i in range(n):
    print(' '*(n-i-1), end='')
    print('*'*(2*i+1))