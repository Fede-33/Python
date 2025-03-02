#El fichero bancos.csv contiene las cotizaciones de los principales bancos de España con : Empresa (nombre de la empresa), Apertura (precio de la acción a la apertura de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Cierre (precio de la acción al cierre de bolsa), Volumen (volumen al cierre de bolsa). Construir una función reciba el fichero bancos.csv y cree un diagrama de líneas con las series temporales de las cotizaciones de cierre de cada banco.

import pandas as pd 
import matplotlib.pyplot as plt 

def evolucion_cotizacion(datos, variable):
    fig, ax = plt.subplots()
    datos.groupby('Empresa').plot(x = 'Fecha', y = variable, ax = ax)
    plt.title('Evolución de las cotizaciones (' + variable + ')')
    plt.legend(df_datos.groupby('Empresa').groups.keys())
    return ax

df_datos = pd.read_csv('./07_files/bancos.csv')
df_datos["Fecha"] = pd.to_datetime(df_datos["Fecha"])
evolucion_cotizacion(df_datos, 'Cierre')
plt.show()