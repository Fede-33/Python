# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

num = int(input('Ingrese un número entero positivo: '))
c = 0

# Rta 1
while c <= num :
    if c%2 != 0 :
        print (c, end=', ')
    c+=1

# Rta 2
for i in range(1, num+1, 2):
    print (i, end=', ')