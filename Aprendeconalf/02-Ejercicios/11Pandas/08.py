# Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv, contienen datos sobre las emisiones contaminates en la ciudad de Madrid en los años 2016, 2017, 2018 y 2019 respectivamente. Escribir un programa con los siguientes requisitos:

import pandas as pd
import numpy as np

#Generar un DataFrame con los datos de los cuatro ficheros.
df2016 = pd.read_csv('./08_files/emisiones-2016.csv', sep=';')
df2017 = pd.read_csv('./08_files/emisiones-2017.csv', sep=';')
df2018 = pd.read_csv('./08_files/emisiones-2018.csv', sep=';')
df2019 = pd.read_csv('./08_files/emisiones-2019.csv', sep=';')
df = pd.concat([df2016, df2017, df2018, df2019])

#Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.
columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES']
columnas.extend([c for c in df if c.startswith('D')])
df = df[columnas]

#Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.
df = df.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')


#Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
df['DIA'] = df.DIA.str.strip('D') #Retirar la letra D del día
df['FECHA'] = df.ANO.apply(str) + '/' + df.MES.apply(str) + '/' + df.DIA.apply(str) #concatenación de columnas en una sola.
df['FECHA'] = pd.to_datetime(df.FECHA, format='%Y/%m/%d', infer_datetime_format=True, errors='coerce') #Transforma la nueva columna en datetime.


#Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones contaminantes y fecha.
df = df.drop(df[np.isnat(df.FECHA)].index) #.isnat, en este caso, verifica valores que no son fecha / .index extrae los índices que retorna isnat / .drop elimina los índices.
df.sort_values(['ESTACION', 'MAGNITUD', 'FECHA'])

#Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
print('Estaciones:', df.ESTACION.unique()) #Unique devuelve
print('Contaminantes:', df.MAGNITUD.unique())

#Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
def consulta (estacion, contaminante, inicio, fin):
    return df[(df.ESTACION == estacion) & (df.MAGNITUD == contaminante) & (df.FECHA >= inicio) & (df.FECHA <= fin)].sort_values('FECHA').VALOR

#Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante.
print(df.groupby('MAGNITUD').VALOR.describe())


#Mostrar un resumen descriptivo para cada contaminante por distritos.
print(df.groupby(['ESTACION', 'MAGNITUD']).VALOR.describe())

#Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada.
def descrip(estacion, contaminante):
    return df[(df.ESTACION == estacion) & (df.MAGNITUD == contaminante)].VALOR.describe()

#Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las estaciones.
def media_mes_porano(contaminante, año):
    return df[(df.MAGNITUD == contaminante) & (df.ANO == año)].groupby(['ESTACION', 'MES']).VALOR.mean().unstack('MES')

#Crear una función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos tipos de contaminantes.
def media_mes_estacion(contaminante, estacion):
    return df[(df.MAGNITUD == contaminante) & (df.ESTACION == estacion)].groupby(['ANO', 'MES']).VALOR.mean().unstack('MES')

