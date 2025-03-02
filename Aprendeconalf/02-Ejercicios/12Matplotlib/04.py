# Escribir una función que reciba una serie de Pandas con el número de ventas de un producto durante los meses de un trimestre y un título y cree un diagrama de sectores con las ventas en formato png con el titulo dado. El diagrama debe guardarse en un fichero con formato png y el título dado.

import pandas as pd
import matplotlib.pyplot as plt

serie = pd.Series(data = {'Enero': 50, 'Febrero': 75, 'Marzo': 60})

def grafico(datos):
    fig, ax = plt.subplots()
    ax.pie(datos)
    ax.set_title('Dado', loc = "center")
    plt.savefig('./04_files/Dado.png') # Guardar el gráfico
    plt.close(fig) # Cierra la figura para liberar memoria

grafico(serie)