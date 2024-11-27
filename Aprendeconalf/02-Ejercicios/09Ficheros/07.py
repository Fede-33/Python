# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).
#Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del fichero por columnas.
#Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el mínimo, el máximo y la media de dada columna.


def diccionario():
    with open('./archivo_cotiz/cotizacion.csv', 'r') as f:
        datos = f.readlines()
        claves = datos[0].split(';')
        claves[-1] = claves[-1].split('\n')[0]
        lista = []
        
        for i in range(1,len(datos)):
            diccionario = {}
            for j in range(len(claves)):
                valores = datos[i].split(';')
                valores[-1] = valores[-1].split('\n')[0]
                diccionario[claves[j]] = valores[j].replace(',', '.')
            lista.append(diccionario)

    return lista
    
def archivo(coleccion):
    with open('./archivo_cotiz/min_max_med.csv', 'w') as f:
        f.write('Nombre;Máximo;Mínimo;Media\n')
        for i in coleccion:
            minimo = float(i['Mínimo'])
            maximo = float(i['Máximo'])
            media = round((minimo + maximo)/2, 2)
            f.write(f"{i['Nombre']};{i['Mínimo']};{i['Máximo']};{media}\n")

archivo(diccionario())