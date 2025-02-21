#Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.

import pandas as pd

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}

def ordenar (n):
    serie = pd.Series(n)
    print(type(serie))
    return serie[serie >=6].sort_values(ascending=True)


print(ordenar(notas))
