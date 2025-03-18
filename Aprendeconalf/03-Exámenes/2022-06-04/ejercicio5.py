# El fichero coches.csv contiene información sobre los modelos de coches vendidos en USA un determinado año. Se pide:

import pandas as pd
import matplotlib.pyplot as plt
import os

    #1 Crear un DataFrame a partir del fichero anterior.

df = pd.read_csv('./5_files/coches.csv', sep=';')

    #2 Eliminar las filas con valores desconocidos y mostrar el número de filas del dataframe resultante.

df = df.dropna() 
print(f'\nNúmero de filas: {df.shape[0]}')

    #3 Crear una columna con el precio en euros (cambio 1$ = 0.94€)

df['Precio€'] = df['Precio']*0.94

    #4 Mostrar por pantalla las 10 últimas filas del DataFrame.

print(f"\nÚltimas 10 filas:\n{df.tail(10)}")

    #5 Mostrar por pantalla el número de marcas que contiene el DataFrame.

print(f"\nNúmero de marcas: {len(df['Marca'].unique())}")

    #6 Mostrar por pantalla el número de modelos de cada marca que hay en el DataFrame, de mayor a menor frecuencia.

print(f"\nNúmero de modelos por marca:\n{df['Marca'].value_counts()}")

    #7 Mostrar por pantalla la marca y el modelo del coche más caro.

print(f"\nCoche más caro: \n{(df[df['Precio'] == df['Precio'].max()])[['Marca', 'Modelo']]}")

    #8 Mostrar por pantalla el precio medio en euros de los coches agrupando por marca y ordenando de menor a mayor precio.

print(f"\nPrecio medio por marca ordenados:\n{round(df.groupby('Marca')['Precio'].mean().sort_values(),2)}")

    #9 Dibujar el diagrama de barras del porcentaje de modelos de cada marca.

porcentaje_marcas = df['Marca'].value_counts() / len(df) * 100
plt.figure(figsize=(10, 6))  
plt.bar(porcentaje_marcas.index, porcentaje_marcas.values)
plt.title('Porcentaje de modelos por marca')
plt.xlabel('Marca')
plt.ylabel('Porcentaje de modelos')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()  

if not os.path.exists('./5_files/gráficos'): #CREAR DIRECTORIO DE GRÁFICOS
    os.makedirs('./5_files/gráficos')
plt.savefig('./5_files/gráficos/porcentaje_modelos_marca.png') #SALVAR EL GRÁFICO
plt.close()

    #10 Dibujar el diagrama de dispersión de la potencia y el precio.

plt.figure(figsize=(10, 6))  
plt.scatter(df['Potencia'], df['Precio'])
plt.title('Diagrama de dispersión: Potencia vs. Precio')
plt.xlabel('Potencia (CV)')
plt.ylabel('Precio (Euros)')
plt.grid(True)

plt.savefig('./5_files/gráficos/dispersion_potencia_precio.png')
plt.close() 

    #11 Los gráficos deben guardarse en una carpeta con el nombre gráficos y deben tener un título adecuado.

    #REALIZADO EN CADA GRÁFICO



