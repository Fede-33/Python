# Ingrese dos números enteros y los muestre ordenados:

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 == num2 :
    print("Los números son iguales. Ordenados: ", num1, num2)
elif num1 < num2 :
    print("Ordenados:", num1, num2)
else :
    print("Ordenados: ", num2, num1)