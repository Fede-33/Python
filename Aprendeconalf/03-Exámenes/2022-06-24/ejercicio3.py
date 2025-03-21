# El fichero bank-loans.csv contiene información sobre los préstamos de los clientes de un banco. Utilizando la librería Pandas, se pide: 

import pandas as pd
import matplotlib.pyplot as plt

    #Crear un DataFrame importando los datos del fichero.
    
df = pd.read_csv('./3_files/bank-loans.csv')

    #Mostrar por pantalla el nombre de las columnas del DataFrame. 

print('\nColumnas:')
for i in df.columns:
    print(f'\t - {i}')
    
    #Mostrar por pantalla las filas del DataFrame múltiplos de 10. 

print('\nFilas múltiplos de 10 :')
print(df.iloc[9::10])

    #Mostrar por pantalla el número de clientes casados con edad entre 30 y 40 años. 
    
print('\nNúmero de clientes casados con edad entre 30 y 40 años:')
print(len(df[(df['marital'] == 'married') & (df['age'] >= 30) & (df['age'] <= 40)]
))

    #Añadir al DataFrame una columna nueva con la edad en meses. 
    
df['edad_meses'] = df['age'] * 12

    #Mostrar por pantalla las frecuencias de los oficios ordenadas de mayor a menor. 

print('\nFrecuencias de los oficios ordenadas de mayor a menor:')    
print(df['job'].value_counts().sort_values(ascending=False))   

    #Mostrar por pantalla las edades medias según el nivel de estudios. 

print('\nEdades medias según el nivel de estudios:')
print(round(df.groupby('education')['age'].mean(),2))

    #Mostrar por pantalla el porcentaje de préstamos hipotecarios (housing) según el estado civil (marital). 

préstamos_marital = df[df['housing'] == 'yes'].groupby('marital').size()
total_marital = df.groupby('marital').size()
print(f'\nporcentaje de préstamos hipotecarios (housing) según el estado civil:\n{round((préstamos_marital / total_marital) * 100,2)}')
    
    #Dibujar el diagrama de sectores con los porcentajes de los niveles de estudio y ponerle un título. 

plt.figure(figsize=(8, 8)) 
plt.pie(df['education'].value_counts(), labels=df['education'].value_counts().index, autopct='%1.1f%%', startangle=140)
plt.title('Porcentaje de Niveles de Estudio')
plt.axis('equal') 
plt.show()

    #Dibujar en una misma figura el histograma y el diagrama de cajas de las edades. El histograma debe tener clases de amplitud 10 desde 20 hasta 70 años, y en color rojo.

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

df['age'].hist(ax=ax1, bins=range(20, 80, 10), color='red')
ax1.set_title('Histograma de Edades')
ax1.set_ylabel('Frecuencia')
ax1.set_xticks(range(20, 80, 10))
ax1.set_xlabel('Edad')

df['age'].plot(kind='box', vert=False, ax=ax2)
ax2.set_title('Diagrama de Cajas de Edades')
ax2.set_xlabel('Edad')

plt.tight_layout()
plt.show()

