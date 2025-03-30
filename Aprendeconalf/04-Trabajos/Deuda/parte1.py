from urllib import request
from urllib.error import URLError

path_deuda = 'https://aprendeconalf.es/docencia/python/trabajos/inteligencia-negocios/datos/deuda.csv'

try:
    f = request.urlopen(path_deuda)
except URLError: 
    print('La URL no existe')
else:
    datos = f.read().decode('utf-8')
    filas = datos.strip().split('\n')
    columnas = filas[0].split(',')
    
#1 Crear una función que reciba un país y un tipo de deuda y devuelva un diccionario con todos los periodos y la cantidad de deuda en esos periodos de ese país y tipo de deuda.
    
    claves = ['Country Code', 'Series Code']
    for i in range(4, len(columnas)):
        claves.append(columnas[i])
    
    data = []
    for i in range(1,len(filas)):
        diccionario = {}
        registro = filas[i].split(',')
        for j in range(len(registro)):
            if columnas[j] in claves:
                diccionario[columnas[j]] = registro[j]
        data.append(diccionario)
    
    def pais_tipo_periodos(data, pais, tipo):
        for i in data:
            if i['Country Code'] == pais and i['Series Code'] == tipo:
                resultado = i.copy()
                del resultado['Country Code']
                del resultado['Series Code']
                return resultado
    
    print(pais_tipo_periodos(data, 'AUS', 'DP.DOD.DLTC.CR.M1.PS.CD'))
    
#2 Crear una función que reciba un país y un tipo de deuda y devuelva un diccionario con el mínimo y el máximo de deuda de ese tipo para ese país.
    
    def pais_tipo_minmax(data, pais, tipo):
        for i in data:
            if i['Country Code'] == pais and i['Series Code'] == tipo:
                resultado = i.copy()
                del resultado['Country Code']
                del resultado['Series Code']
                minimo = min(resultado.items(), key=lambda item: item[1])
                maximo = max(resultado.items(), key=lambda item: item[1])
        
        return {minimo, maximo}
                
    print(pais_tipo_minmax(data, 'AUS', 'DP.DOD.DLTC.CR.M1.PS.CD'))
    
#3 Crear una función que reciba un país y un año, y devuelva un diccionario con la deuda interna y la deuda externa de ese país en ese año.
    
    def sumar_year(diccionario, year):
        suma = 0
        for j in range(len(diccionario.keys())):
            if year in str(list(diccionario.keys())[j]):
                if diccionario[list(diccionario.keys())[j]] != '':
                    suma += float(diccionario[list(diccionario.keys())[j]]) 
        return suma
    
    def pais_deuda_intext(data, pais, year):
        deudas = {}
        for i in data:
            if i['Country Code'] == pais:
                if i['Series Code'] == 'DP.DOD.DECD.CR.PS.CD':
                    deudas['interna'] = sumar_year(i, year)
                if i['Series Code'] == 'DP.DOD.DECX.CR.PS.CD':
                    deudas['externa'] = sumar_year(i, year)
        return deudas
    
    print(pais_deuda_intext(data, 'AUS', '2015'))
               
#4 Crear una función que reciba un país y un año, y devuelva un diccionario con la deuda en moneda local y la deuda en moneda extranjera de ese país en ese año.
    
    def pais_deuda_divisas(data, pais, year):
        deudas = {}
        for i in data:
            if i['Country Code'] == pais:
                if i['Series Code'] == 'DP.DOD.DECN.CR.PS.CD':
                    deudas['moneda local'] = sumar_year(i, year)
                if i['Series Code'] == 'DP.DOD.DECF.CR.PS.CD':
                    deudas['moneda extranjera'] = sumar_year(i, year)
        return deudas
    
    print(pais_deuda_divisas(data, 'AUS', '2015'))


