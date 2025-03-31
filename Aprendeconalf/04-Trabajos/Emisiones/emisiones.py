from urllib.error import HTTPError
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

magnitudes = {'01':'Dióxido de Azufre','06':'Monóxido de Carbono','07':'Monóxido de Nitrógeno','08':'Dióxido de Nitrógeno','09':'Partículas < 2.5 μm','10':'Partículas < 10 μm','12':'Óxidos de Nitrógeno','14':'Ozono','20':'Tolueno','30':'Benceno','35':'Etilbenceno','37':'Metaxileno','38':'Paraxileno','39':'Ortoxileno','42':'Hidrocarburos totales(hexano)','43':'Metano','44':'Hidrocarburosno metánicos (hexano)'}

estaciones = {'001':'Pº. Recoletos','002':'Glta. de Carlos V','035':'Pza. del Carmen','004':'Pza. de España','039':'Barrio del Pilar','006':'Pza. Dr. Marañón','007':'Pza. M. de Salamanca','008':'Escuelas Aguirre','009':'Pza. Luca de Tena','038':'Cuatro Caminos','011':'Av. Ramón y Cajal','012':'Pza. Manuel Becerra','040':'Vallecas','014':'Pza. Fdez. Ladreda','015':'Pza. Castilla','016':'Arturo Soria', '017':'Villaverde Alto','018':'Calle Farolillo','019':'Huerta Castañeda','036':'Moratalaz','021':'Pza. Cristo Rey','022':'Pº. Pontones','023':'Final C/ Alcalá','024':'Casa de Campo','025':'Santa Eugenia','026':'Urb. Embajada (Barajas)','027':'Barajas','047':'Méndez Álvaro','048':'Pº. Castellana','049':'Retiro','050':'Pza. Castilla','054':'Ensanche Vallecas','055':'Urb. Embajada (Barajas)','056':'Plaza Elíptica','057':'Sanchinarro','058':'El Pardo','059':'Parque Juan Carlos I','060':'Tres Olivos'}

try:
    df = pd.read_csv('https://aprendeconalf.es/docencia/python/trabajos/inteligencia-negocios/datos/emisiones-madrid.csv')
except HTTPError:
    print('La url no existe')
else:
    df = df.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
    df['DIA'] = df['DIA'].apply(lambda x: x[1:])
    df['ESTACION'] = df['ESTACION'].astype(str)
    df['MAGNITUD'] = df['MAGNITUD'].astype(str)
    df['MES'] = df['MES'].astype(str)
    df['ANO'] = df['ANO'].astype(str)
    df['ESTACION'] = df['ESTACION'].apply(
        lambda x: '00' + x if len(x) < 2 else '0' + x)
    df['MAGNITUD'] = df['MAGNITUD'].apply(lambda x: '0' + x if len(x) < 2 else x)
    df['MES'] = df['MES'].apply(lambda x: '0' + x if len(x) < 2 else x)
    df['FECHA'] = df['DIA'] + '/' + df['MES'] + '/' + df['ANO']
    df['FECHA'] = pd.to_datetime(df['FECHA'], format='%d/%m/%Y', errors='coerce')
    df = df.drop(df[np.isnat(df['FECHA'])].index)
    df = df.sort_values(['FECHA', 'MAGNITUD', 'ESTACION'])

#1 Crear una función que reciba una estación de medición y una magnitud y devuelva una lista con todas las mediciones de la magnitud en la estación.

    def obtener_mediciones(df, estacion, magnitud):
  
        df_filtrado = df[(df['ESTACION'] == estacion) & (df['MAGNITUD'] == magnitud)]
        return list(df_filtrado['VALOR'])
    
    print(obtener_mediciones(df, '050', '12'))

#2 Crear una función que reciba un mes y una estación de medición y devuelva un diccionario con las medias de las magnitudes medidas por la estación durante ese mes.

    def medias_mes_estacion(df, mes, estacion):

        df1 = df[(df['ESTACION'] == estacion) & (df['MES'] == mes)]
        return {magnitudes[k]:np.mean(v) for k, v in df1.groupby('MAGNITUD')['VALOR']}

    print(medias_mes_estacion(df, '03', '050'))

#3 Crear una función que reciba un mes y una magnitud y devuelva un diccionario con las medias de las estaciones de medición de la magnitud durante ese mes.

    def medias_mes_magnitud(df, mes, magnitud):
        df1 = df[(df['MAGNITUD'] == magnitud) & (df['MES'] == mes)]    
        return {estaciones[k]:np.mean(v) for k, v in df1.groupby('ESTACION')['VALOR']}
                                                                             
    print(medias_mes_magnitud(df, '12', '12'))

#4 Crear una función que reciba un rango de fechas y una estación de medición y genere un gráfico con la evolución diaria de las magnitudes de esa estación en las fechas indicadas.

    def evolucion_estacion(df, estacion, inicio, fin):

        df['NOMBRE MAGNITUD'] = df['MAGNITUD'].apply(lambda x: magnitudes[x])
        df1 = df[(df['ESTACION'] == estacion) & (df['FECHA'] >= inicio) & (df['FECHA'] <= fin)]
        df1.set_index('FECHA', inplace = True)
        
        fig, ax = plt.subplots()
        df1.groupby('NOMBRE MAGNITUD')['VALOR'].plot(legend = True)
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])
        plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
        return plt.show()
        
    evolucion_estacion(df, '017', '2018-03-01', '2018-06-30')

#5 Crear una función que reciba un rango de fechas y una magnitud y genere un gráfico con la evolución diaria de la magnitud para cada estación de medición en las fechas indicadas.

    def evolucion_magnitud(df, magnitud, inicio, fin):

        df['NOMBRE ESTACION'] = df['ESTACION'].apply(lambda x: estaciones[x])
        df1 = df[(df['MAGNITUD'] == magnitud) & (df['FECHA'] >= inicio) & (df['FECHA'] <= fin)]
        df1.set_index('FECHA', inplace = True)
        fig, ax = plt.subplots()
        df1.groupby('NOMBRE ESTACION')['VALOR'].plot(legend = True)
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])
        plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
        return plt.show()

    evolucion_magnitud(df, '12', '2018-03-01', '2018-06-30')

#6 Crear una función que reciba una magnitud y genere un gráfico con las medias mensuales para cada estación de medición.

    def grafico_medias_mensuales_magnitud(df, magnitud):

        df_magnitud = df[df['MAGNITUD'] == magnitud]
        medias_mensuales = df_magnitud.groupby(['NOMBRE ESTACION', 'ANO', 'MES'])['VALOR'].mean().unstack(level='NOMBRE ESTACION')

        plt.figure(figsize=(14, 8))
        medias_mensuales.plot(marker='o', ax=plt.gca())
        plt.title(f'Medias Mensuales de la Magnitud {magnitud}')
        plt.xlabel('Año-Mes')
        plt.ylabel('Valor Medio')
        plt.xticks(rotation=45)
        plt.legend(title='Estación', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout(rect=[0, 0, 0.9, 1])
        plt.grid(True)
        return plt.show()
    
    print(grafico_medias_mensuales_magnitud(df, '12'))

#7 Crear una función que reciba un mes y una magnitud y devuelva un diccionario con las medias de la magnitud dentro de Madrid Central y fuera de ella.

    def medias_magnitud_por_area(df, mes, magnitud):
        df_filtrado = df[(df['MES'] == mes) & (df['MAGNITUD'] == magnitud)]

        estaciones_central = ['004', '008', '017', '018', '024']  
        estaciones_fuera = [estacion for estacion in df_filtrado['ESTACION'].unique() if estacion not in estaciones_central]

        media_central = df_filtrado[df_filtrado['ESTACION'].isin(estaciones_central)]['VALOR'].mean()
        media_fuera = df_filtrado[df_filtrado['ESTACION'].isin(estaciones_fuera)]['VALOR'].mean()

        return {'Madrid Central': media_central, 'Fuera de Madrid Central': media_fuera}

    print(medias_magnitud_por_area(df, '12', '12'))

#8 Crear una función que reciba una magnitud y genere un gráfico con las medias mensuales dentro de Madrid Central y fuera de ella.

    def grafico_medias_mensuales_por_area(df, magnitud):
        df_magnitud = df[df['MAGNITUD'] == magnitud].copy()
        estaciones_central = ['004', '008', '017', '018', '024']  #(Lista de ejemplo)
        df_magnitud['AREA'] = df_magnitud['ESTACION'].apply(lambda x: 'Madrid Central' if x in estaciones_central else 'Fuera de Madrid Central')

        medias_mensuales = df_magnitud.groupby(['AREA', 'ANO', 'MES'])['VALOR'].mean().unstack(level='AREA')

        plt.figure(figsize=(14, 8))
        medias_mensuales.plot(marker='o', ax=plt.gca())
        plt.title(f'Medias Mensuales de la Magnitud {magnitud} por Área')
        plt.xlabel('Año-Mes')
        plt.ylabel('Valor Medio')
        plt.xticks(rotation=45)
        plt.legend(title='Área', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout(rect=[0, 0, 0.9, 1])
        plt.grid(True)
        return plt.show()
    
    print(grafico_medias_mensuales_por_area(df, '12'))

print(df)