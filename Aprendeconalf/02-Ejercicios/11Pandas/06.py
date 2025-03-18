# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros). Construir una función que construya un DataFrame a partir de un fichero con el formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.

import pandas as pd

def resumen (direc):
    df = pd.read_csv(direc, sep=';', decimal=',', thousands='.', index_col = 0)
    return pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])

print(resumen('./06_files/cotizacion.csv'))

#Para utilizar este método, es necesario especificar los separadores numéricos de unidades de mil y decimales. También es indispensable especificar que el ìndice del DataFrame será la columna 0, porque esta contiene los nombres de las empresas. Si no se especifica index_col = 0, entonces la columna 0 pasará a ser parte de los cálculos, y siendo los datos alfanuméricos, provocará un error al intentar realizar los cálculos.



