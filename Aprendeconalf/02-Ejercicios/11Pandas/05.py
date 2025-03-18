# Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.

import pandas as pd

diccionario = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 
               'Ventas':[30500, 35600, 28300, 33900],  
               'Gastos': [22000, 23400, 18100, 20700]}

balances = []

for i in range(len(diccionario['Ventas'])):
    balances.append(diccionario['Ventas'][i]-diccionario['Gastos'][i])

df = pd.DataFrame(diccionario)
df['Balance'] = balances

print(df)