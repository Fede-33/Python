# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

num = None
while num == None:
    try:
        num = int(input('Ingrese número entero positivo: '))
        if num <= 0:
            num = None
            raise RuntimeError
    except (ValueError, RuntimeError):
        print('Incorrecto.\n')

for i in range(1,num+1,2):
    print(i)