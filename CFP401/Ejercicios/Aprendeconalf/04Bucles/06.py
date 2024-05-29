# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

num = None
while num == None:
    try:
        num = int(input('Ingrese altura del triángulo (entero positivo): '))
        if num <= 0 :
            num = None
            raise ValueError
    except ValueError:
        print('Incorrecto.\n')

for i in range(num):
    print('*'*(i+1))