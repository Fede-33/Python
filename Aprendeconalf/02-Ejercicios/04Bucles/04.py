# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

num = None
while num == None:
    try:
        num = int(input('Ingrese un número entero positivo:'))
        if num <= 0:
            num = None
            raise RuntimeError
    except(ValueError, RuntimeError):
        print('Incorrecto.\n')

for i in range(num,-1, -1):
    print(i, end=', ')