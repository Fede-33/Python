# Crea un programa que pida al usuario que introduzca su nombre y un número entero, y
# escriba su nombre en pantalla tantas veces como indique ese número entero.

nomb = input("Ingrese su nombre: ")
num = int(input("Ingrese un número entero: "))

while num != 0 :
	print(nomb)
	num -= 1