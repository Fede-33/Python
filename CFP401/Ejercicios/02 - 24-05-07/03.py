# Crea un programa que pida al usuario que introduzca el resultado de la suma entre 13 y 5. 
# El programa se deberá repetir hasta que introduzca el resultado correcto


rta = 0

while rta != '18' and rta != 'dieciocho' :
	rta = input("¿Cuánto es 13 + 5? ").lower()

print("Respuesta correcta.")