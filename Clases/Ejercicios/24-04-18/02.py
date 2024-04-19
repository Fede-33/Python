#Ingresar un número y definir si es positivo, negativo o 0

num = float(input("Ingrese un número: "))
if num > 0 :
    print ("El número", num, "es positivo")
elif num == 0:
    print ("El número es 0")
else: 
    print ("El número", num, "es negativo")