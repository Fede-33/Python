# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

password = 'contraseña'
ingreso = None

while ingreso != password:
    ingreso = input('Ingrese contraseña: ')