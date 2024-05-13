#Ingresar dos números enteros y muestre su división

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

if divisor == 0 :
    print ("No se puede dividir por 0.")
else:
    print (dividendo / divisor)