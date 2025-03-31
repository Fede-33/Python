from urllib import request
from urllib.error import URLError
import pandas as pd
import matplotlib.pyplot as plt

try:
    f = request.urlopen('https://aprendeconalf.es/docencia/python/trabajos/inteligencia-negocios/datos/contratos-menores-madrid.csv')
except URLError: 
    print('La URL no existe')
else:
    datos = f.read().decode('utf-8')
    filas = datos.strip().split('\n')
    columnas = filas[0].split(';')

    datos = []
    for i in range(1, len(filas)):
        registro = {}
        for j in range(len(columnas)):
            registro[columnas[j]] = filas[i].split(';')[j]
            if columnas[j] == 'IMPORTE' or columnas[j] == 'AÑO':
                try:
                    registro[columnas[j]] = float(registro[columnas[j]])
                except ValueError:
                    registro[columnas[j]] = float(filas[i].split(';')[j+1])    
        datos.append(registro)

#1 Crear una función que reciba una empresa y una lista de años y devuelva un diccionario con el número de contratos y el total facturado por la empresa esos años.

    def empresa_year(lista, empresa, year):
        contador = 0
        suma = 0

        for i in lista:
            if i['AÑO'] in year and i['CONTRATISTA'] == empresa:
                contador += 1
                suma += i['IMPORTE']

        return{'Número de contratos': contador, 'Total facturado': round(suma,2)}

    print(empresa_year(datos, 'SUCESORES DE DIONISIO GARCIA GOMEZ S.L.', [2018, 2019]))

#2 Crear una función que reciba una sección y una lista de años y devuelva un diccionario con el número de contratos y el total facturado a la sección esos años.

    def seccion_year(lista, seccion, year):
        contador = 0
        suma = 0

        for i in lista:
            if i['AÑO'] in year and i['SECCION'] == seccion:
                contador += 1
                suma += i['IMPORTE']

        return{'Número de contratos': contador, 'Total gastado': round(suma,2)}

    print(seccion_year(datos, 'EMPRESA MUNICIPAL DE TRANSPORTES S.A.', [2018, 2019]))

#3 Crear una función que reciba una empresa, una sección y una lista de años y devuelva un diccionario con el número de contratos y el total facturado por la empresa a la sección esos años.

    def empresa_seccion_year(lista, empresa, seccion, year):
        contador = 0
        suma = 0

        for i in lista:
            if i['AÑO'] in year and i['SECCION'] == seccion and i['CONTRATISTA'] == empresa:
                contador += 1
                suma += i['IMPORTE']

        return{'Número de contratos': contador, 'Total facturado': round(suma,2)}

    print(empresa_seccion_year(datos, 'CARROCERIAS BUS, S.L.', 'EMPRESA MUNICIPAL DE TRANSPORTES S.A.', [2018, 2019]))

#4 Crear una función que reciba una rango de años y un número entero n e imprima la lista de las n empresas que más han facturado durante esos años ordenadas de mayor a menor facturación y genere un gráfico con esa información.

    df= pd.DataFrame(data=datos)
    
    def empresas_facturacion(df, year, n):

        df_filtrado = df[df['AÑO'].isin(year)]

        resultado = df_filtrado.groupby('CONTRATISTA')['IMPORTE'].sum().sort_values(ascending=False).head(n)

        print(f"Las {n} empresas con mayor facturación en los años {year} son:")
        for empresa, facturacion in resultado.items():
            print(f"- {empresa}: {facturacion:.2f}")

        plt.figure(figsize=(10, 6))
        resultado.plot(kind='bar')
        plt.title(f"Top {n} Empresas con Mayor Facturación ({year})")
        plt.xlabel("Empresa")
        plt.ylabel("Facturación Total")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        return plt.show()

    print(empresas_facturacion(df, [2018,2019], 10))

#5 Crear una función reciba una rango de años y un número entero n y genere un gráfico con la evolución anual del total facturado por las n empresas que más han facturado.

    def evolucion_facturacion_empresas(df, year, n):

        df_filtrado = df[df['AÑO'].isin(range(year[0], year[1]+1))]

        n_empresas = df_filtrado.groupby('CONTRATISTA')['IMPORTE'].sum().sort_values(ascending=False).head(n).index
        df_top_n = df_filtrado[df_filtrado['CONTRATISTA'].isin(n_empresas)]
        facturacion_anual = df_top_n.groupby(['CONTRATISTA', 'AÑO'])['IMPORTE'].sum().unstack()

        plt.figure(figsize=(12, 8))
        facturacion_anual.T.plot(ax=plt.gca(), marker='o')  
        plt.title(f'Evolución Anual de Facturación de las {n} Empresas Principales ({year})')
        plt.xlabel('Año')
        plt.ylabel('Facturación Total')
        plt.xticks(facturacion_anual.columns)  
        plt.legend(title='Empresa')
        plt.grid(True)
        plt.tight_layout()
        return plt.show()

    print(evolucion_facturacion_empresas(df, [2017, 2019], 10))
   
#6 Crear una función reciba una rango de años y genere un gráfico con la evolución anual del total facturado a las secciones.

    def evolucion_facturacion_secciones(df, year):

        df_filtrado = df[df['AÑO'].isin(range(year[0], year[1]+1))]

        facturacion_anual_seccion = df_filtrado.groupby(['SECCION', 'AÑO'])['IMPORTE'].sum().unstack()

        plt.figure(figsize=(20, 15))
        facturacion_anual_seccion.T.plot(ax=plt.gca(), marker='o')  
        plt.title(f'Evolución Anual de Facturación por Secciones ({year})')
        plt.xlabel('Año')
        plt.ylabel('Facturación Total')
        plt.xticks(facturacion_anual_seccion.columns) 
        plt.legend(title='Sección', bbox_to_anchor=(1.05, 1), loc='upper left') 
        plt.grid(True)
        plt.tight_layout(rect=[0, 0, 0.9, 1]) 
        plt.show()
    
    print(evolucion_facturacion_secciones(df, [2017,2019]))

