# El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Crear un dataframe con Pandas y a partir de él generar los siguientes diagramas.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./08_files/titanic.csv')

#Diagrama de sectores con los fallecidos y supervivientes.

fig, ax = plt.subplots()
labels = ['Fallecidos', 'Supervivientes']
ax.pie(df.Survived.value_counts(), labels = labels)
ax.set_title ('Distribución de supervivientes', loc = 'center')
plt.show()

#Histograma con las edades.

fig, ax = plt.subplots()
ax.hist(df.Age)
ax.set_title ('Histograma de edades', loc = 'center')
plt.show()

#Diagrama de barras con el número de personas en cada clase.

class_counts = df.Pclass.value_counts().sort_index() # Ordena los valores de Pclass.
fig, ax = plt.subplots()
labels = ['Primera', 'Segunda', 'Tercera']
ax.bar(class_counts.index, class_counts.values)  # Pasa los índices y los valores a ax.bar()
ax.set_xticks(class_counts.index) # Establece las posiciones de las etiquetas en el eje x
ax.set_xticklabels(labels) # Establece las etiquetas del eje x
ax.set_title ('Número de personas por clase', loc = 'center')
plt.show()

#Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.

df.groupby(["Pclass", "Survived"]).size().unstack().plot(kind = "bar", title = "Número de personas fallecidas y supervivientes por clase")
plt.show()

#Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.

df.groupby(["Pclass", "Survived"]).size().unstack().plot(kind = "bar", stacked = True, title = "Número de personas fallecidas y supervivientes por clase")
plt.show()

