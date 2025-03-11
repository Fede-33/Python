# Crear un programa utilizando la librería Pandas y Matplotlib que realice lo siguiente:

import pandas as pd
import matplotlib.pyplot as plt

    #1 Crear el siguiente DataFrame indexado:

datos = {
  "Calorias": [420, 380, 390, 490, 300],
  "Tiempo": [60, 40, 75, 55, 45]
}
semana = ["L", "M", "X", "J", "V"]
df = pd.DataFrame(datos, semana)

    #2 Calcular la media, mediana y desviación típica de ambas columnas.

print(df.mean())
print(df.median())
print(df.std())

    #3 Añadir otra columna booleana al DataFrame para ver si se ha cumplido el reto de quemar más de 400 calorías por hora. La nueva columna debe generarse aplicando una fórmula a las otras columnas. El DataFrame resultante debe ser el siguiente:

df['Reto'] = df.Calorias / df.Tiempo > 400 / 60
print(df)

    #4 Filtrar el DataFrame y devolver otro DataFrame con las filas pares que cumplan que el número de calorías es mayor de 400.
    
df_pares = df.iloc[range(0, df.shape[0], 2)]
df_pares_mayor_400 = df_pares[df_pares.Calorias > 400]
print(df_pares_mayor_400)    
    
    #5 Crear a partir del DataFrame una serie con los porcentajes de días que se ha conseguido el reto y los que no.
    
print(df.Reto.value_counts(normalize = True) * 100)    
    
    #6 Crear un gráfico como el de más abajo que muestre la progresión de las calorías y tiempo durante la semana.

fig, ax = plt.subplots()
df.plot(y = 'Calorias', marker = "+", ax = ax)
df.plot(y = 'Tiempo', marker = "o", ax = ax)
plt.title('Evolución diaria')
plt.show()