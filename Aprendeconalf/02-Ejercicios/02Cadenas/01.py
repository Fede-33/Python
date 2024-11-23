# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nom = input('Ingrese su nombre: ')
num = int(input('Ingrese número de veces a repetir: '))

print((f'{nom} \n') * num)