import pandas as pd
import matplotlib.pyplot as plt
from urllib.error import HTTPError
import seaborn as sns

path_deuda = 'https://aprendeconalf.es/docencia/python/trabajos/inteligencia-negocios/datos/deuda.csv'
path_pib = 'https://aprendeconalf.es/docencia/python/trabajos/inteligencia-negocios/datos/pib.csv'

#1 Preprocesar el fichero de deuda pública para obtener un data frame con el país, el tipo de deuda, la fecha y la cantidad de deuda.

try:
    df_deuda = pd.read_csv(path_deuda)
except HTTPError:
    print('La url no existe')
else:

    col_fecha = df_deuda.columns[4:]
    df_deuda = df_deuda.melt(id_vars=['Country Name', 'Country Code', 'Series Name', 'Series Code'], value_vars=col_fecha, var_name='Fecha', value_name='Deuda')
    df_deuda['Fecha'] = df_deuda['Fecha'].str[0:6]
    df_deuda.rename(columns={'Country Name': 'Pais', 'Country Code': 'PaisId','Series Name': 'Tipo', 'Series Code': 'TipoId'}, inplace=True)
    tipos = {'DP.DOD.DECD.CR.PS.CD': 'Deuda interna', 'DP.DOD.DECN.CR.PS.CD': 'Deuda en moneda local', 'DP.DOD.DECX.CR.PS.CD': 'Deuda externa', 'DP.DOD.DECF.CR.PS.CD': 'Deuda en moneda extranjera', 'DP.DOD.DLTC.CR.M1.PS.CD': 'Deuda a lago plazo', 'DP.DOD.DSTC.CR.PS.CD': 'Deuda a corto plazo'}
    df_deuda['TipoId'] = df_deuda.TipoId.apply(lambda x: tipos[x] if x in tipos.keys() else x)

    df_deuda['Deuda'] = pd.to_numeric(df_deuda['Deuda'], errors='coerce')
    df_deuda.dropna(subset=['Deuda'], inplace=True)
        
#2 Crear una función que reciba un país y una fecha y devuelva un diccionario con la deuda total interna, externa, en moneda local, en moneda extranjera, a corto plazo y a largo plazo, de ese país en esa fecha.

    def deuda_pais_fecha(dataframe, pais_consulta, fecha_consulta):
        
        filtro = (dataframe['PaisId'] == pais_consulta) & (dataframe['Fecha'] == fecha_consulta)
        df_filtrado = dataframe[filtro]
        deuda_total = {}
        tipos_deuda = ['Deuda interna', 'Deuda externa', 'Deuda en moneda local', 'Deuda en moneda extranjera', 'Deuda a corto plazo', 'Deuda a largo plazo']
        for tipo in tipos_deuda:
            deuda_tipo = df_filtrado[df_filtrado['TipoId'] == tipo]['Deuda'].sum()
            deuda_total[tipo] = deuda_tipo

        return deuda_total

    print(deuda_pais_fecha(df_deuda, 'AUS', '2015Q1'))

#3 Crear una función que reciba un tipo de deuda y una fecha, y devuelva un diccionario con la deuda de ese tipo de todos los países en esa fecha.

    def deuda_tipo_fecha(dataframe, tipo_consulta, fecha_consulta):

            filtro = (dataframe['TipoId'] == tipo_consulta) & (dataframe['Fecha'] == fecha_consulta)
            df_filtrado = dataframe[filtro]

            deuda_paises = {}
            for pais in df_filtrado['Pais'].unique():
                deuda = df_filtrado[df_filtrado['Pais'] == pais]['Deuda'].sum()
                deuda_paises[pais] = deuda

            return deuda_paises

    print(deuda_tipo_fecha(df_deuda, 'Deuda externa', '2015Q1'))

#4 Crear una función que reciba un país y una fecha y dibuje un diagrama de sectores con la deuda interna y la deuda externa de ese país en esa fecha.

    def sectores_deuda_interna_externa(dataframe, pais_consulta, fecha_consulta):
        
        filtro = (dataframe['PaisId'] == pais_consulta) & (dataframe['Fecha'] == fecha_consulta) & (dataframe['TipoId'].isin(['Deuda interna', 'Deuda externa']))
        df_filtrado = dataframe[filtro]

        if df_filtrado.empty:
            print(f"No hay datos de deuda interna y externa para {pais_consulta} en {fecha_consulta}.")
            return

        deuda_por_tipo = df_filtrado.groupby('TipoId')['Deuda'].sum()

        plt.figure(figsize=(8, 6))
        plt.pie(deuda_por_tipo, labels=deuda_por_tipo.index, autopct='%1.1f%%', startangle=140)
        plt.title(f'Deuda Interna vs. Externa en {pais_consulta} ({fecha_consulta})')
        plt.axis('equal')
        return plt.show()

    print (sectores_deuda_interna_externa(df_deuda, 'AUS', '2015Q1'))

#5 Crear una función que reciba un país y una fecha, y dibuje un diagrama de barras con las cantidades de los distintos tipos de deudas de ese país en esa fecha.

    def barras_deuda_tipos(dataframe, pais_consulta, fecha_consulta):

        filtro = (dataframe['PaisId'] == pais_consulta) & (dataframe['Fecha'] == fecha_consulta)
        df_filtrado = dataframe[filtro]

        if df_filtrado.empty:
            print(f"No hay datos de deuda para {pais_consulta} en {fecha_consulta}.")
            return

        deuda_por_tipo = df_filtrado.groupby('TipoId')['Deuda'].sum()

        plt.figure(figsize=(10, 6))
        deuda_por_tipo.plot(kind='bar')
        plt.title(f'Deuda por Tipo en {pais_consulta} ({fecha_consulta})')
        plt.xlabel('Tipo de Deuda')
        plt.ylabel('Cantidad de Deuda')
        plt.xticks(rotation=45, ha='right') 
        plt.tight_layout()  
        return plt.show()
    
    barras_deuda_tipos(df_deuda, 'AUS', '2015Q1')

#6 Crear una función que reciba una lista de países y un tipo de deuda y dibuje un diagrama de líneas con la evolución de ese tipo de deuda de esos países (una línea por país).

    def lineas_evolucion_deuda(dataframe, paises_consulta, tipo_consulta):

        filtro = (dataframe['PaisId'].isin(paises_consulta)) & (dataframe['TipoId'] == tipo_consulta)
        df_filtrado = dataframe[filtro]

        if df_filtrado.empty:
            print(f"No hay datos de {tipo_consulta} para los países especificados.")
            return

        plt.figure(figsize=(12, 6))
        for pais in paises_consulta:
            df_pais = df_filtrado[df_filtrado['PaisId'] == pais]
            plt.plot(df_pais['Fecha'], df_pais['Deuda'], label=pais)

        plt.title(f'Evolución de {tipo_consulta} por País')
        plt.xlabel('Fecha')
        plt.ylabel('Cantidad de Deuda')
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        return plt.show()
        
    
    print(lineas_evolucion_deuda(df_deuda, ['GEO', 'SLV', 'MDA'], 'Deuda interna'))

#7 Crear una función que reciba un país y una lista de tipos de deuda y dibuje un diagrama de líneas con la evolución de esos tipos de deuda de ese país (una línea por tipo de deuda).

    def lineas_evolucion_deuda_tipos(dataframe, pais_consulta, tipos_consulta):

        filtro = (dataframe['PaisId'] == pais_consulta) & (dataframe['TipoId'].isin(tipos_consulta))
        df_filtrado = dataframe[filtro]

        if df_filtrado.empty:
            print(f"No hay datos de deuda para {pais_consulta} y los tipos especificados.")
            return

        plt.figure(figsize=(12, 6))
        for tipo in tipos_consulta:
            df_tipo = df_filtrado[df_filtrado['TipoId'] == tipo]
            plt.plot(df_tipo['Fecha'], df_tipo['Deuda'], label=tipo)

        plt.title(f'Evolución de la Deuda en {pais_consulta}')
        plt.xlabel('Fecha')
        plt.ylabel('Cantidad de Deuda')
        plt.xticks(rotation=45, ha='right')  # Rotar etiquetas para mejor legibilidad
        plt.legend()
        plt.tight_layout()
        return plt.show()
    
    print(lineas_evolucion_deuda_tipos(df_deuda, 'SLV', ['Deuda interna', 'Deuda externa']))

#8 Crear una función que reciba una lista de países y una lista de tipos de deuda, y dibuje un diagrama de cajas con las deudas de esos tipos de esos países (una caja por país y tipo de deuda).

    def dibujar_cajas_deuda(dataframe, paises_consulta, tipos_consulta):


        filtro = (dataframe['PaisId'].isin(paises_consulta)) & (dataframe['TipoId'].isin(tipos_consulta))
        df_filtrado = dataframe[filtro]

        if df_filtrado.empty:
            print(f"No hay datos de deuda para los países y tipos especificados.")
            return

        plt.figure(figsize=(14, 8))
        sns.boxplot(x='TipoId', y='Deuda', hue='Pais', data=df_filtrado)
        plt.title('Distribución de la Deuda por País y Tipo')
        plt.xlabel('Tipo de Deuda')
        plt.ylabel('Cantidad de Deuda')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        return plt.show()
    
    print(dibujar_cajas_deuda(df_deuda, ['BOL', 'MDA', 'SLV'], ['Deuda interna', 'Deuda externa']))

#9 Preprocesar el fichero del PIB crear un data frame con el país, la fecha y el PIB.

try:
    df_pib = pd.read_csv(path_pib)
except HTTPError:
    print('La url no existe')
else:

    col_fecha = df_pib.columns[4:]
    df_pib = df_pib.melt(id_vars=['Country Name', 'Country Code'], value_vars=col_fecha, var_name='Fecha', value_name='PIB')
    df_pib['Fecha'] = df_pib['Fecha'].str[0:4]
    df_pib.rename(columns={'Country Name': 'Pais', 'Country Code': 'PaisId'}, inplace=True)
   
    df_pib['PIB'] = pd.to_numeric(df_pib['PIB'], errors='coerce')
    df_pib.dropna(subset=['PIB'], inplace=True)

    print(df_pib)

#10 Crear una función que reciba un país y dibuje la evolución de la deuda pública total como porcentaje del PIB.

    def grafico_deuda_pib(dataframe_deuda, dataframe_pib, pais_consulta):

        df_pais_deuda = dataframe_deuda[dataframe_deuda['PaisId'] == pais_consulta]
        df_pais_pib = dataframe_pib[dataframe_pib['PaisId'] == pais_consulta]

        df_deuda_anual = df_pais_deuda.groupby(df_pais_deuda['Fecha'].str[:4])['Deuda'].sum().reset_index()
        df_deuda_anual.rename(columns={'Fecha': 'Año', 'Deuda': 'Deuda_Total'}, inplace=True)

        df_combinado = pd.merge(df_deuda_anual, df_pais_pib, left_on='Año', right_on='Fecha')

        if df_combinado.empty:
            print(f"No hay datos disponibles para {pais_consulta}.")
            return

        df_combinado['Deuda_PIB'] = (df_combinado['Deuda_Total'] / df_combinado['PIB']) * 100

        plt.figure(figsize=(12, 6))
        plt.plot(df_combinado['Año'], df_combinado['Deuda_PIB'])
        plt.title(f'Deuda Pública como % del PIB en {pais_consulta}')
        plt.xlabel('Año')
        plt.ylabel('Deuda como % del PIB')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        return plt.show()

    print(grafico_deuda_pib(df_deuda, df_pib, 'AUS'))

#11 Crear una función que reciba un país devuelva un diccionario con los años y si el endeudamiento en esa fecha era insostenible. Se considera un endeudamiento insostenible si durante los tres años anteriores el porcentaje de deuda pública con respecto al PIB es superior al 20%.

    def endeudamiento_insostenible(dataframe_deuda, dataframe_pib, pais_consulta):

        df_pais_deuda = dataframe_deuda[dataframe_deuda['PaisId'] == pais_consulta]
        df_pais_pib = dataframe_pib[dataframe_pib['PaisId'] == pais_consulta]

        df_deuda_anual = df_pais_deuda.groupby(df_pais_deuda['Fecha'].str[:4])['Deuda'].sum().reset_index()
        df_deuda_anual.rename(columns={'Fecha': 'Año', 'Deuda': 'Deuda_Total'}, inplace=True)

        df_combinado = pd.merge(df_deuda_anual, df_pais_pib, left_on='Año', right_on='Fecha')

        if df_combinado.empty:
            print(f"No hay datos disponibles para {pais_consulta}.")
            return {}

        df_combinado['Deuda_PIB'] = (df_combinado['Deuda_Total'] / df_combinado['PIB']) * 100

        resultado = {}
        for i in range(len(df_combinado)):
            anio = df_combinado['Año'][i]
            if i >= 3:
                deuda_pib_ultimos_tres_anios = df_combinado['Deuda_PIB'][i-3:i].values
                insostenible = all(deuda_pib > 20 for deuda_pib in deuda_pib_ultimos_tres_anios)
                resultado[anio] = insostenible
            else:
                resultado[anio] = False  

        return resultado

    print(endeudamiento_insostenible(df_deuda, df_pib, 'AUS'))