#1 Extraer del fichero de alojamientos una lista con todos los alojamientos, donde cada alojamiento sea un diccionario que contenga el identificador del alojamiento, el identificador del anfitrión, el distrito, el precio y las plazas.

with open('./madrid-airbnb-listings-small.csv', 'r', encoding='utf-8') as f:
    lineas = f.readlines()
    columnas = lineas[0].strip().split('\t')
    titulos = ['id', 'host_id', 'neighbourhood_group_cleansed', 'accommodates', 'price']
    alojamientos = []

for i in range(1, len(lineas)):
    diccionario = {}
    for j in range(len(columnas)):
        if columnas[j] in titulos:
            diccionario[columnas[j]] = lineas[i].split('\t')[j]
    alojamientos.append(diccionario)

#2 Crear una función que reciba la lista de alojamientos y devuelva el número de alojamientos en cada distrito.

def cantidad(lista):
    diccionario = {}
    for i in lista:
        try:
            diccionario[i['neighbourhood_group_cleansed']] += 1
        except:
            diccionario[i['neighbourhood_group_cleansed']] = 1
    return diccionario

#3 Crear una función que reciba la lista de alojamientos y un número de ocupantes y devuelva la lista de alojamientos con un número de plazas mayor o igual que el número de ocupantes.

def ocupantes(lista, nro):
    resultado = []
    for i in lista:
        if int(i['accommodates']) >= nro:
            resultado.append(i)
    return resultado

#4 Crear una función que reciba la lista de alojamientos un distrito, y devuelva los 10 alojamientos más baratos del distrito.

def baratos(lista, dist):
    resultado = []
    for i in lista:
        if i['neighbourhood_group_cleansed'] == dist :
            resultado.append(i)
        resultado = sorted(resultado, key = lambda resultado: float(resultado['price'][1:]))
    return resultado[:10]

#5 Crear una función que reciba la lista de alojamientos y devuelva un diccionario con los anfitriones y el número de alojamientos que posee cada uno.

def anfitriones(lista):
    diccionario = {}
    for i in lista:
        try:
            diccionario[i['host_id']] += 1
        except:
            diccionario[i['host_id']] = 1
    return diccionario

print(anfitriones(alojamientos))
