# Escribir una función que calcule el módulo de un vector.

def modulo (variables):
    sumatoria = 0
    for i in variables:
        sumatoria = sumatoria + (i**2)
    return sumatoria**0.5

lista =[]
rep = int(input("Ingrese cantidad de variables: "))
for i in range(rep):
    lista.append(int(input("Ingrese variable: ")))


print (modulo (lista))