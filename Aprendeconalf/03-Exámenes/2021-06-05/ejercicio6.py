# Construir un programa que realize las siguientes operaciones con la librería Pandas:

import pandas as pd
import matplotlib.pyplot as plt

    #1 Crear un DataFrame con las siguientes columnas:

    #Nombre: Juan, Marta, Pedro, Jorge, Blas, Lisa, Antonio
    #Edad: 23,78,22,19,45,33,20
    #Género: M, F, M, M, M, F, M
    #Provincia’: Burgos, Madrid, Toledo, Burgos, Madrid, Toledo, Madrid
    #Hijos: 2,0,0,3,2,1,4
    #Mascotas: 5,1,0,5,2,2,3
    
diccionario = {
            'Nombre': ['Juan', 'Marta', 'Pedro', 'Jorge', 'Blas', 'Lisa', 'Antonio'],
            'Edad': [23, 78, 22, 19, 45, 33, 20],
            'Género': ['M', 'F', 'M', 'M', 'M', 'F', 'M'],
            'Provincia': ['Burgos', 'Madrid', 'Toledo', 'Burgos', 'Madrid', 'Toledo', 'Madrid'],
            'Hijos': [2, 0, 0, 3, 2, 1, 4],
            'Mascotas': [5, 1, 0, 5, 2, 2, 3]
            }

df = pd.DataFrame(diccionario)

    #2 Mostrar la información básica del DataFrame.

print(df.info())

    #3 Obtener los principales estadísticos de las columnas numéricas.

print(df.describe())

    #4 Obtener los porcentajes de hombres y mujeres por provincias.

print(df.groupby('Provincia').Género.value_counts(normalize = True) * 100)

    #5 Representar, mediante un diagrama de dispersión, en número de hijos frente al número de mascotas para las personas de Madrid.

fig, ax = plt.subplots()
df[df.Provincia == 'Madrid'].plot(kind = 'scatter', x = 'Hijos', y = 'Mascotas', ax = ax)
plt.show()

    #6 Realizar la siguiente gráfica.

fig, ax = plt.subplots()
df.groupby('Provincia').size().plot(kind = 'bar')
plt.title('Distribución de frecuencias por provincia')
plt.show()