# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n(n+1)/2)

n = int(input('Ingrese un número entero positivo: '))

print(f'la suma de todos los números enteros hasta {n} es', n*(n+1)/2)