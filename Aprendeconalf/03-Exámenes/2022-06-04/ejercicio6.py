# El fichero bitcoin-tweets.csv contiene los tweets obtenidos en una búsqueda en Twitter sobre bitcoins (cada línea contiene información de un tweet). Se pide:

from urllib import request

path = 'https://aprendeconalf.es/docencia/python/examenes/inteligencia-negocios/soluciones/examen-2022-06-04/bitcoin-tweets.csv'

    #1 Crear una función que reciba la url de un fichero csv como el anterior y devuelva una lista con los tweets del fichero, donde cada tweet se represente con un diccionario con sus campos, tal y como se muestra en la siguiente salida:

def abrir(ruta):
    f = request.urlopen(ruta)
    lineas = f.readlines()
    lista = []

    for i in range(1, len(lineas)):
        linea = lineas[i].decode('utf-8').strip().split(';')
        diccionario = {}
        for j in range(len(linea)):
            diccionario[lineas[0].decode('utf-8').strip().split(';')[j].replace('\n', '')] = linea[j].replace("b'", "").replace("\\", "")
        lista.append(diccionario)

    return lista

    #2 Crear una función que reciba una lista de tweets como la que devuelve la función anterior, y devuelva un diccionario con los hashtags contenidos en los tweets y su frecuencia, tal y como se muestra en la siguiente salida:

def hashtags(lista):
    dicc_hash={}

    for i in lista:
        listext = i['texto'].split(' ')
        for j in listext:
            if j.startswith('#'):
                try:
                    dicc_hash[j] += 1
                except KeyError:
                    dicc_hash[j] = 1

    return dicc_hash

print(hashtags(abrir(path)))