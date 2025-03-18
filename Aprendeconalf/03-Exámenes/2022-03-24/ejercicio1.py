# Escriba un programa que permita practicar una variante simplificada de la prueba de cálculo mental La calculadora humana del concurso televisivo Saber y ganar. El usuario debe ir sumando todos los números de la lista de uno en uno hasta que se equivoque o termine la lista, en cuyo caso ganará.

import random as rd

num = 0
cont = 0
print ('Comience a sumar los números empezando desde 0 + ')

while True:
    aleatorio = rd.randint(1,100)
    num += aleatorio
    respuesta = int(input(f'Más {aleatorio}: '))
    if respuesta != num:
        break
    cont += 1

print(f'Has acertado {cont} veces.')

    


