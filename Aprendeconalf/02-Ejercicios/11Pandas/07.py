# El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:

import pandas as pd

fichero = './07_files/titanic.csv'

#Generar un DataFrame con los datos del fichero.
df = pd.read_csv(fichero, sep=',', decimal='.')

#Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
print(f'Dimensiones del DataFrame:\n   {df.shape[0]} Filas\n   {df.shape[1]} Columnas')
print(f'\nEl DataFrame contiene {df.size} datos')

print(f'\nSus columnas son:')
columnas = list(df.columns)
tipos = list(df.dtypes)
for i in (range(len(columnas))):
    print(f'   {columnas[i]} del tipo {tipos[i]}')

print('\n10 primeras filas:')
print(df.head(10))
print('\n10 últimas filas:')
print(df.tail(10))

#Mostrar por pantalla los datos del pasajero con identificador 148.
print('\nEl pasajero con identificación 148 era:')
print(df[(df['PassengerId']==148)])

#Mostrar por pantalla las filas pares del DataFrame.
print('\nFilas pares del DataFrame:')
print(df.iloc[range(0,df.shape[0],2)])

#Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print('\nPasajeros en primera clase:')
print(df[(df['Pclass']==1)].sort_values('Name', ascending=True))

#Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
vivos = df['Survived'].value_counts()[1]
fallecidos = df['Survived'].value_counts()[0]
cant = df.shape[0]
print(f'\nEl porcentaje general de sobrevivientes es de:{(vivos/cant*100).round(2)}')
print(f'El porcentaje general de víctimas fatales es de:{(fallecidos/cant*100).round(2)}')

#Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.

def sobrev(datos):
    cant = datos.shape[0]
    vivos = datos['Survived'].value_counts()[1]
    return (vivos/cant*100).round(2)

for i in range(1,4):
    print(f'\nEl porcentaje de sobrevivientes en clase {i} es de {sobrev(df[(df['Pclass']==i)])}')

#Eliminar del DataFrame los pasajeros con edad desconocida.
df.dropna(subset=['Age']) 

#Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
print(df.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])

#Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
df['Minor'] = df['Age']<18

#Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
print(df.groupby(['Pclass', 'Minor'])['Survived'].value_counts(normalize = True) * 100)