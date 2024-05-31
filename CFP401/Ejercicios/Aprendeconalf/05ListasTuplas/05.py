# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

nums = []

for i in range (1,11):
    nums.append(i)

nums.sort(reverse=True)
print(nums)