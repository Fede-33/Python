# Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.

import pandas as pd

inicio = int(input('Ingrese año de inicio: '))
fin = int(input('Ingrese año de cierre: '))
ventas = {}

for i in range(inicio, fin+1):
    ventas[i] = float(input(f'Ingrese las ventas del año {i}: '))

serie = pd.Series(data = ventas)

print(f'DATOS DE LAS VENTAS:\n {serie}')
print(f'VENTAS CON DESCUENTO:\n {serie*0.9}')