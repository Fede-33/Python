# Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.

import pandas as pd

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}

serienotas = pd.Series(data = notas)
seriestats = pd.Series({'Nota Mínima' : serienotas.min(), 'Nota Máxima' : serienotas.max(), 'Media' : serienotas.mean(), 'Desviación típica' : serienotas.std()})

print(seriestats)