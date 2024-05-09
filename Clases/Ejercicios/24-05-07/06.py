# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contras = ''
verif = ''

while (contras == verif) :
	contras = input("Ingrese su contraseña: ")

while (contras != verif) :
	verif = input("Repita su contraseña: ")

print("Contraseña confirmada.")
