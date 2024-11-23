# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

carrito = input('Ingrese artículos separados por coma: ')

print(carrito.replace(',', '\n'))
