# El fichero cercanias.csv contiene información sobre las líneas de tren de cercanías de Madrid: id (identificador del tren), línea (nombre de la línea), estaciones (estaciones de origen y destino separadas por un guion). Se pide:

    #1 Construir una función que lea el fichero cercanias.csv y cree un diccionario donde la clave de cada par sea el identificador de la línea y el valor asociado una lista de dos elementos con la estación de origen y la estación de destino.La función debe recibir el nombre del fichero como parámetro. 

path = './5_files/cercanias.csv'
path_2 = './5_files/resultado.csv'

def leer (ruta):

    diccionario = {}

    with open(ruta, 'r') as f:
        lineas = f.readlines()

    for i in range(1, len(lineas)):
        linea = lineas[i].split(',')
        dest = linea[2].replace('\n','').split('-')
        
        diccionario[linea[0]] = [dest[0], dest[1]]
        
    return diccionario

    # 2 Construir otra función que guarde la información del diccionario obtenido en el apartado anterior en un fichero csv separado por punto y coma con 3 columnas con los encabezados id, origen y destino. La función debe recibir como parámetros el diccionario con los trenes y el nombre del fichero resultante.

def escribir(diccionario, ruta):

    with open(ruta,'w') as f:
        f.write('id;origen;destino')

        for i in diccionario.keys():
            f.write(f'\n{i};{diccionario[i][0]};{diccionario[i][1]}')


escribir(leer(path), path_2)