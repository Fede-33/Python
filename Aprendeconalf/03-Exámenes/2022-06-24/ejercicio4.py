# El fichero bank-loans.csv contiene información sobre los préstamos de los clientes de un banco. Utilizando ficheros (sin usar la librería Pandas), crear una función que tenga como parámetros la url del fichero, el nombre de una columna cualitativa y un booleano para los porcentajes (False por defecto), que devuelva un diccionario con las frecuencias absolutas de las categorías de la columna indicada. Si se pasa True como argumento del parámetro para el porcentaje, la función debe devolver el diccionario de porcentajes de las categorías. 

from urllib import request

path = 'https://aprendeconalf.es/docencia/python/examenes/inteligencia-negocios/soluciones/examen-2022-06-24/bank-loans.csv'

def frecuencias(ruta, columna, porc = False):
    f = request.urlopen(ruta)
    lineas = f.readlines()
    indice = (lineas[0].decode('utf-8').strip().split(',')).index(columna)
    diccionario = {}

    for i in range(1, len(lineas)):
        linea = lineas[i].decode('utf-8').strip().split(',')
        try:
            diccionario[linea[indice]] += 1
        except KeyError:
             diccionario[linea[indice]] = 1

    if porc :
        total = sum(diccionario.values())
        for i in diccionario.keys():
            diccionario[i] = diccionario[i] * 100/ total

    return diccionario

print(frecuencias(path, 'education'))
print(frecuencias(path, 'housing', True))