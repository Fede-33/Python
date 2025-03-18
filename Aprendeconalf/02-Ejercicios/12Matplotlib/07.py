#El fichero bancos.csv contiene las cotizaciones de los principales bancos de España con : Empresa (nombre de la empresa), Apertura (precio de la acción a la apertura de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Cierre (precio de la acción al cierre de bolsa), Volumen (volumen al cierre de bolsa). Construir una función reciba el fichero bancos.csv y cree un diagrama de líneas con las series temporales de las cotizaciones de cierre de cada banco.

import pandas as pd
import matplotlib.pyplot as plt

def grafico(datos):
    fig, ax = plt.subplots()
    for i in datos.columns :
        ax.plot(datos.index, datos[i], label=i)
    ax.legend(loc = 'lower right')
    plt.show()

df = pd.read_csv('./07_files/bancos.csv', sep=',', decimal='.', index_col = 0)
df = df.drop(columns=['Apertura', 'Máximo', 'Mínimo', 'Volumen'])
df = df.pivot_table(index='Fecha', columns='Empresa', values='Cierre')

grafico(df)