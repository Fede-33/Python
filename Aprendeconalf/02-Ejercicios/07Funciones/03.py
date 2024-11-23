#Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(num):
    mult = 1
    for i in range(num):
        mult *= i+1
    return mult

numero = int(input('Ingrese un número: '))

print(f'Su factorial es {factorial(numero)}')