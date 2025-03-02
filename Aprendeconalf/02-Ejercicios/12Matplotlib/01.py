#Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla un diagrama de líneas con la evolución de las ventas.

import pandas as pd
import matplotlib.pyplot as plt

inicio = int(input('Ingrese año de inicio: '))
fin = int(input('Ingrese año de cierre: '))
ventas = {}

for i in range(inicio, fin+1):
    ventas[i] = float(input(f'Ingrese las ventas del año {i}: '))

serie = pd.Series(data = ventas)

fig, ax = plt.subplots()
ax.plot(serie)
plt.show()