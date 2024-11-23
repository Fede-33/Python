# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

vocales = ('a', 'e', 'i', 'o', 'u')

ingreso = input('Ingrese una frase: ')

frase = list(ingreso)

for i in vocales:
    c = 0
    for j in frase:
        if j == i:
            c += 1
    if c == 0:
        print(f'La letra {i} no está en la frase.')
    else: 
        print(f'La letra {i} se repite {c} veces.')

