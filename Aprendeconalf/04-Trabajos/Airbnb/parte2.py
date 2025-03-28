import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from langdetect import detect, LangDetectException

#1 Preprocesar el fichero de alojamientos para crear un data frame con las variables id, host_id, listing_url, room_type, neighbourhood_group_cleansed, price, cleaning_fee, accommodates, minimum_nights, minimum_cost, review_scores_rating, latitude, longitude, is_location_exact. Eliminar del data frame cualquier fila incompleta. Añadir al data frame nuevas variables con el coste mínimo por noche y por persona (que incluya los gastos de limpieza).

columnas = ['id', 'host_id', 'listing_url', 'room_type', 'neighbourhood_group_cleansed', 'price', 'cleaning_fee', 'accommodates', 'minimum_nights', 'review_scores_rating', 'latitude', 'longitude', 'is_location_exact']

df = pd.read_csv('./madrid-airbnb-listings-small.csv', sep = '\t', usecols = columnas).dropna()
df['price'] = pd.to_numeric(df['price'].str.replace('$', '', regex=False), errors='coerce')
df['cleaning_fee'] = pd.to_numeric(df['cleaning_fee'].str.replace('$', '', regex=False), errors='coerce')
df['min_price_per_cap'] = ((df['price'] * df['minimum_nights'] + df['cleaning_fee']) / (df['minimum_nights'] + df['accommodates']))

#2 Crear una función que reciba una lista de distritos y devuelva un diccionario con los tipos de alojamiento en ese distrito y el porcentaje de alojamientos de ese tipo.

def tipos_distrito(df, lista):
    df = df[df['neighbourhood_group_cleansed'].isin(lista)]
    porcentajes = (df['room_type'].value_counts() / len(df)) * 100
    resultado = porcentajes.to_dict()
    return resultado

print(tipos_distrito(df, ['Arganzuela', 'Centro']))

#3 Crear una función que reciba una lista de distritos y devuelva un diccionario con el número de alojamientos que cada anfitrión ofrece en esos distrito, ordenado de más a menos alojamientos.

def anfitrion_distrito(df, lista):
    df= df[df['neighbourhood_group_cleansed'].isin(lista)]
    resultado = df['host_id'].value_counts().to_dict()
    resultado = dict(sorted(resultado.items(), key=lambda item: item[1], reverse=True))
    return resultado

print(anfitrion_distrito(df, ['Centro']))
print(anfitrion_distrito(df, ['Villaverde']))

#4 Crear una función que reciba devuelva un diccionario con el número medio de alojamientos por anfitrión de cada distrito.

def promedio_anfitrion_distrito(df):
    alojamientos_por_anfitrion_distrito = df.groupby(['neighbourhood_group_cleansed', 'host_id']).size()
    promedio_por_distrito = alojamientos_por_anfitrion_distrito.groupby('neighbourhood_group_cleansed').mean()
    resultado = promedio_por_distrito.to_dict()
    return resultado

print(promedio_anfitrion_distrito(df))

#5 Crear una función que reciba una lista de distritos y dibuje un diagrama de sectores con los porcentajes de tipos de alojamientos en esos distritos.

def sectores_tipos(df, lista):
    df = df[df['neighbourhood_group_cleansed'].isin(lista)].copy()
    porcentajes = (df['room_type'].value_counts() / len(df)) * 100

    plt.figure(figsize=(8, 8))
    plt.pie(porcentajes, labels=porcentajes.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Porcentaje de Tipos de Alojamiento en {", ".join(lista)}')
    plt.axis('equal')  
    return plt.show()

sectores_tipos(df, ['Arganzuela', 'Centro'], )

#6 Crear una función que dibuje un diagrama de barras con el número de alojamientos por distritos.

def barras_cantidad_distrito(df):
    alojamientos_por_distrito = df['neighbourhood_group_cleansed'].value_counts()

    plt.figure(figsize=(10, 6))
    plt.bar(alojamientos_por_distrito.index, alojamientos_por_distrito.values)
    plt.xlabel('Distrito')
    plt.ylabel('Número de alojamientos')
    plt.title('Número de Alojamientos por Distrito')
    plt.xticks(rotation=90, ha='right')  

    plt.tight_layout()  
    return plt.show()

barras_cantidad_distrito(df)

#7 Crear una función que dibuje un diagrama de barras con los porcentajes acumulados de tipos de alojamientos por distritos.

def barras_porcentaje_distrito(df):
    porcentaje_por_distrito = df.groupby('neighbourhood_group_cleansed')['room_type'].value_counts(normalize=True).mul(100).unstack()
    porcentaje_acumulado = porcentaje_por_distrito.cumsum(axis=1)

    plt.figure(figsize=(12, 8))
    porcentaje_acumulado.plot(kind='bar', stacked=True, ax=plt.gca())
    plt.xlabel('Distrito')
    plt.ylabel('Porcentaje Acumulado de Alojamientos')
    plt.title('Porcentaje Acumulado de Tipos de Alojamientos por Distrito')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Tipo de Alojamiento')
    plt.tight_layout()
    return plt.show()

barras_porcentaje_distrito(df)

#8 Crear una función reciba una lista de distritos y una lista de tipos de alojamientos, y dibuje un diagrama de sectores con la distribución del número de alojamientos de ese tipo por anfitrión.

def sectores_distrito_tipo(df, dist, tipos):
    df = df[df['neighbourhood_group_cleansed'].isin(dist) & df['room_type'].isin(tipos)]
    alojamientos_por_anfitrion = df['host_id'].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(alojamientos_por_anfitrion, labels=alojamientos_por_anfitrion.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribución de Alojamientos ({", ".join(tipos)}) por Anfitrión en {", ".join(dist)}')
    plt.axis('equal')
    return plt.show()

sectores_distrito_tipo(df, ['Villaverde', 'Vicálvaro'], ['Entire home/apt', 'Hotel room'])

#9 Crear una función que dibuje un diagrama de barras con los precios medios por persona y día de cada distrito.

def barras_promedio_persona_distrito(df):
    df['precio_por_persona_dia'] = df['price'] / df['accommodates']
    precio_medio_por_distrito = df.groupby('neighbourhood_group_cleansed')['precio_por_persona_dia'].mean()

    plt.figure(figsize=(10, 6))
    plt.bar(precio_medio_por_distrito.index, precio_medio_por_distrito.values)
    plt.xlabel('Distrito')
    plt.ylabel('Precio Medio por Persona y Día')
    plt.title('Precio Medio por Persona y Día por Distrito')
    plt.xticks(rotation=90, ha='right')  

    plt.tight_layout()
    return plt.show()

barras_promedio_persona_distrito(df)

#10 Crear una función que reciba una lista de distritos y dibuje un gráfico de dispersión con el coste mínimo por noche y persona y la puntuación en esos distritos.

def disper_costeminimo_punt(df, lista):
    df = df[df['neighbourhood_group_cleansed'].isin(lista)].copy()
    df['coste_minimo_persona_noche'] = df['price'] / df['accommodates'] / df['minimum_nights']

    plt.figure(figsize=(10, 6))
    plt.scatter(df['coste_minimo_persona_noche'], df['review_scores_rating'])
    plt.xlabel('Coste Mínimo por Noche y Persona')
    plt.ylabel('Puntuación')
    plt.title(f'Coste Mínimo por Noche y Persona vs. Puntuación en {", ".join(lista)}')
    return plt.show()

disper_costeminimo_punt(df, ['Arganzuela', 'Centro'])

#11 Crear una función que reciba una lista de distritos y dibuje dos histogramas con la distribución de precios por persona y día, uno para los alojamientos con título en inglés y otro para los alojamientos con títulos en español. Si la distribución es muy asimétrica, aplicar una transformación logarítmica. ¿Hay diferencias entre los precios de los alojamientos en inglés y el español? Nota: Para identificar el idioma puede usare el módulo langdetect.

def histogramas_precios_idioma(df, lista):
    df = df[df['neighbourhood_group_cleansed'].isin(lista)].copy()
    df['precio_por_persona_dia'] = df['price'] / df['accommodates']

    def detectar_idioma(titulo):
        if pd.isna(titulo) or len(titulo) < 3:
            return None
        try:
            return detect(titulo)
        except LangDetectException:
            return None

    df['idioma_titulo'] = df['listing_url'].apply(detectar_idioma)

    df_ingles = df[df['idioma_titulo'] == 'en'].copy()
    df_espanol = df[df['idioma_titulo'] == 'es'].copy()

    if not df_ingles.empty:
        if df_ingles['precio_por_persona_dia'].skew() > 1 or df_ingles['precio_por_persona_dia'].skew() < -1:
            df_ingles.loc[:, 'precio_por_persona_dia'] = np.log1p(df_ingles['precio_por_persona_dia'])
            titulo_ingles = 'Distribución de Precios por Persona y Día (Inglés, Log)'
        else:
            titulo_ingles = 'Distribución de Precios por Persona y Día (Inglés)'
    else:
        titulo_ingles = "No hay datos en ingles"

    if not df_espanol.empty:
        if df_espanol['precio_por_persona_dia'].skew() > 1 or df_espanol['precio_por_persona_dia'].skew() < -1:
            df_espanol.loc[:, 'precio_por_persona_dia'] = np.log1p(df_espanol['precio_por_persona_dia'])
            titulo_espanol = 'Distribución de Precios por Persona y Día (Español, Log)'
        else:
            titulo_espanol = 'Distribución de Precios por Persona y Día (Español)'
    else:
        titulo_espanol = "No hay datos en español"

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    if not df_ingles.empty:
        plt.hist(df_ingles['precio_por_persona_dia'], bins=20)
    plt.xlabel('Precio por Persona y Día')
    plt.ylabel('Frecuencia')
    plt.title(titulo_ingles)

    plt.subplot(1, 2, 2)
    if not df_espanol.empty:
        plt.hist(df_espanol['precio_por_persona_dia'], bins=20)
    plt.xlabel('Precio por Persona y Día')
    plt.ylabel('Frecuencia')
    plt.title(titulo_espanol)

    plt.tight_layout()
    plt.show()

histogramas_precios_idioma(df, ['Arganzuela', 'Centro'])