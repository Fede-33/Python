#Ingresar tres números reales distintos y mostrar el mayor:

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 == num2 or num1 == num3 or num2 == num3 :
    print ("Los números no deben ser iguales.")
else :
    if num1 > num2 and num1 > num3:
        print ("El mayor es:", num1)
    elif num2 > num1 and num2 > num3:
        print ("El mayor es:", num2)
    else :
        print ("El mayor es:", num3)
