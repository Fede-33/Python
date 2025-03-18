# Escribir una función que reciba una serie de Pandas con el número de ventas de un producto por años y una cadena con el tipo de gráfico a generar (lineas, barras, sectores, areas) y devuelva un diagrama del tipo indicado con la evolución de las ventas por años y con el título “Evolución del número de ventas”.

import pandas as pd
import matplotlib.pyplot as plt

def grafico(datos, tipo):
    graficos = {'lineas':'line', 'barras':'bar', 'sectores':'pie', 'area':'area'}
    fig, ax = plt.subplots()
    datos.plot(kind = graficos[tipo], ax = ax)
    plt.title('Evolución del número de ventas')
    plt.show()

serie = pd.Series({2010:50, 2011:30, 2012:35, 2013:30, 2014:40, 2015:55})
tipo = 'area'

grafico(serie, tipo)
