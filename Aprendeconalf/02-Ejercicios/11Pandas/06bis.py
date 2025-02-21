# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros). Construir una función que construya un DataFrame a partir de un fichero con el formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de dada fila.

import pandas as pd
import statistics as stat


def dfmean (direc):
    df = pd.read_csv(direc, sep=';', decimal=',')
    df2 = df[['Nombre','Mínimo','Máximo']]
    
    medias = []
    for i in df.index :
        tupla = (df2.loc[i, ('Mínimo')], df2.loc[i, 'Máximo'])
        medias.append(stat.mean(tupla))

    
    df2['Media'] = medias
    
    return df2

print(dfmean('./06_files/cotizacion.csv'))



