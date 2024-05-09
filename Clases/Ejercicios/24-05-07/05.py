# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla todos los números impares desde 1 hasta ese número separados por comas.

num = int(input("Ingrese un número entero positivo: "))

cont = 0
lista = []

while (cont != num) :
	if (cont%2 != 0) :
		lista.append(cont)
	cont += 1	

print(lista)	
		