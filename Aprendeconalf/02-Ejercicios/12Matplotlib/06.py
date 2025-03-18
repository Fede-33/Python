#Escribir una función que reciba un dataframe de Pandas con los ingresos y gastos de una empresa por meses y devuelva un diagrama de líneas con dos líneas, una para los ingresos y otra para los gastos. El diagrama debe tener una leyenda identificando la línea de los ingresos y la de los gastos, un título con el nombre “Evolución de ingresos y gastos” y el eje y debe empezar en 0.

import pandas as pd
import matplotlib.pyplot as plt

def grafico (df):
    fig, ax = plt.subplots()
    ax.plot(df['Mes'], df['Ingresos'], label='Ingresos')
    ax.plot(df['Mes'], df['Gastos'], label='Gastos')
    plt.title('Evolución de ingresos y gastos', loc = 'center')
    ax.set_ylim([0, max(df.Ingresos.max(), df.Gastos.max()) + 500])
    ax.legend(loc = 'lower right')
    plt.show()


df = pd.DataFrame({'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ingresos':[30500, 35600, 28300, 33900],  'Gastos': [22000, 23400, 18100, 20700]})

grafico(df)