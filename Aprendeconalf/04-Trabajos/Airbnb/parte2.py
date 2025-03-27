import pandas as pd
import matplotlib as plt

#1 Preprocesar el fichero de alojamientos para crear un data frame con las variables id, host_id, listing_url, room_type, neighbourhood_group_cleansed, price, cleaning_fee, accommodates, minimum_nights, minimum_cost, review_scores_rating, latitude, longitude, is_location_exact. Eliminar del data frame cualquier fila incompleta. Añadir al data frame nuevas variables con el coste mínimo por noche y por persona (que incluya los gastos de limpieza).

columnas = ['id', 'host_id', 'listing_url', 'room_type', 'neighbourhood_group_cleansed', 'price', 'cleaning_fee', 'accommodates', 'minimum_nights', 'review_scores_rating', 'latitude', 'longitude', 'is_location_exact']

df = pd.read_csv('./madrid-airbnb-listings-small.csv', sep = '\t', usecols = columnas).dropna()
df['price'] = pd.to_numeric(df['price'].str.replace('$', '', regex=False), errors='coerce')
df['cleaning_fee'] = pd.to_numeric(df['cleaning_fee'].str.replace('$', '', regex=False), errors='coerce')
df['min_price_per_cap'] = ((df['price'] * df['minimum_nights'] + df['cleaning_fee']) / (df['minimum_nights'] + df['accommodates']))

print(df)




#2 Crear una función que reciba una lista de distritos y devuelva un diccionario con los tipos de alojamiento en ese distrito y el porcentaje de alojamientos de ese tipo.



#3 Crear una función que reciba una lista de distritos y devuelva un diccionario con el número de alojamientos que cada anfitrión ofrece en esos distrito, ordenado de más a menos alojamientos.



#4 Crear una función que reciba devuelva un diccionario con el número medio de alojamientos por anfitrión de cada distrito.



#5 Crear una función que reciba una lista de distritos y dibuje un diagrama de sectores con los porcentajes de tipos de alojamientos en esos distritos.



#6 Crear una función que dibuje un diagrama de barras con el número de alojamientos por distritos.



#7 Crear una función que dibuje un diagrama de barras con los porcentajes acumulados de tipos de alojamientos por distritos.



#8 Crear una función reciba una lista de distritos y una lista de tipos de alojamientos, y dibuje un diagrama de sectores con la distribución del número de alojamientos de ese tipo por anfitrión.



#9 Crear una función que dibuje un diagrama de barras con los precios medios por persona y día de cada distrito.



#10 Crear una función que reciba una lista de distritos y dibuje un gráfico de dispersión con el coste mínimo por noche y persona y la puntuación en esos distritos.



#11 Crear una función que reciba una lista de distritos y dibuje dos histogramas con la distribución de precios por persona y día, uno para los alojamientos con título en inglés y otro para los alojamientos con títulos en español. Si la distribución es muy asimétrica, aplicar una transformación logarítmica. ¿Hay diferencias entre los precios de los alojamientos en inglés y el español? Nota: Para identificar el idioma puede usare el módulo langdetect.
