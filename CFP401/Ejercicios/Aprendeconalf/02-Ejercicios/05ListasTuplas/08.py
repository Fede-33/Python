# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

ingreso = input('Ingrese una palabra: ')

palabra = list(ingreso.lower())
palrev = list(ingreso.lower())
palrev.reverse()


if palabra == palrev:
    print(f'{ingreso} es un palíndromo')
else:
    print(f'{ingreso} no es un palíndromo')