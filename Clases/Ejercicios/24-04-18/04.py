# Ingrese dos números reales y muestre el mayor de ellos

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 > num2 :
    print ("El número", num1, "es mayor que", num2)
elif num1 == num2 :
    print ("Los números", num1, "y", num2, "son iguales.")
else:
    print ("El número", num2, "es mayor que", num1)     