# Escribir una función que reciba una diccionario con las notas de las asignaturas de un curso y una cadena con el nombre de un color y devuelva un diagrama de barras de las notas en el color dado.

import pandas as pd
import matplotlib.pyplot as plt

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
color = 'green'

serienotas = pd.Series(data = notas)

def grafico (notas, tono):
    fig, ax = plt.subplots()
    ax.bar(notas.index, notas.values, color = tono)
    plt.show()

grafico(serienotas, color)