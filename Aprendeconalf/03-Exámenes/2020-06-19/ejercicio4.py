#El fichero ipc-2020.csv contiene el IPC de las comunidades autónomas de los cinco primeros meses de 2020. Crear un programa que realice las siguientes operaciones utilizando la librería Pandas:

import pandas as pd

    #1 Crear un DataFrame leyendo el fichero desde internet con la url https://aprendeconalf.es/docencia/python/examenes/inteligencia-negocios/soluciones/examen-2020-06-19/ipc-2020.csv.

df = pd.read_csv('https://aprendeconalf.es/docencia/python/examenes/inteligencia-negocios/soluciones/examen-2020-06-19/ipc-2020.csv')

    #2 Mostrar por pantalla el DataFrame con los datos de las filas 10 a 15.

print(df.iloc[10:16])

    #3 Mostrar por pantalla el DataFrame con los datos de Canarias de Mayo.

print(df[(df['Comunidad autónoma'] == 'Canarias') & (df['Mes'] == 'Mayo')])

    #4 Mostrar por pantalla una serie con el IPC mensual máximo de cada comunidad autónoma.

print(df.groupby('Comunidad autónoma')['IPC'].max())

    #5 Mostrar por pantalla una serie con la desviación típica del IPC mensual de cada grupo.

print(df.groupby('Grupo')['IPC'].std())

    #6 Mostrar por pantalla un DataFrame con las comunidades y grupos donde los precios no han subido en promedio (IPC mensual medio menor de 100).

ipc_medio_por_comunidad_grupo = df.groupby(['Comunidad autónoma', 'Grupo'])['IPC'].mean()
comunidades_grupos_sin_subida = ipc_medio_por_comunidad_grupo[ipc_medio_por_comunidad_grupo < 100]
comunidades_grupos_sin_subida_df = comunidades_grupos_sin_subida.reset_index()
print(comunidades_grupos_sin_subida_df)