# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = input('Ingrese precio: \N{euro sign}')

pagar = precio.split(',')
print(f'Debe pagar \N{euro sign}{pagar[0]} con {pagar[1]} centavos.')