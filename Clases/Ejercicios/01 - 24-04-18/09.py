#Ingresar una edad y calcular el valor de la entrada menor a 4 años entra gratis, entre 4 y 18 paga 5€ y mayor 10€

edad = int(input("Ingrese la edad: "))

if edad < 0 :
    print ("Edad incorrecta.")
elif edad < 4 :
    print ("Entrada gratuita.")
elif edad <= 18:
    print ("Debe abonar 5€.")
else :
    print ("Debe abonar 10€.")