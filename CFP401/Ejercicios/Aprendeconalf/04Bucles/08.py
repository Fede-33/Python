# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

num = None
while num == None:
    try:
        num = int(input('Ingrese altura del triángulo (entero positivo): '))
        if num <= 0 :
            num = None
            raise ValueError
    except ValueError:
        print('Incorrecto.\n')

for i in range (num+1):
    for j in range(i*2, 0, -1):
        if j % 2 == 1 :
            print(j, end=' ')
    print('\n')