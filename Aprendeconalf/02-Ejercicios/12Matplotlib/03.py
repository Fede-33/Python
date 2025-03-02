#Escribir una función que reciba una serie de Pandas con las notas de los alumnos de un curso y devuelva un diagrama de cajas con las notas. El diagrama debe tener el título “Distribución de notas”.

import pandas as pd
import matplotlib.pyplot as plt

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}

serienotas = pd.Series(data = notas)

def grafico (notas):
    fig, ax = plt.subplots()
    ax.boxplot(notas)
    ax.set_title('Distribución de notas', loc = "center")
    plt.show()

grafico(serienotas)