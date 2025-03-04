# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).

#Construir una función que abra un fichero con el formato anterior y devuelva un diccionario con los datos del fichero por columnas.La función debe cumplir los siguientes requisitos:

    #La función recibirá como único parámetro la ruta del fichero.
    #Debe realizarse un preprocesado de los datos que reemplace la coma por el punto como separador de decimales.
    #Debe realizarse el control de errores mediante excepciones para el caso de que el fichero no exista en la ruta indicada.
    #Debe devolver un diccionario con tantos elementos como columnas tenga el fichero, donde la clave de cada par sea el nombre de la columna y el valor la lista de datos de la columna.

import statistics as st

path = './5_files/cotizacion.csv'

def abrir(ruta):
    try:
        with open(ruta, 'r') as f:
            archivo = f.readlines()
            archivo = [i.replace(".", "") for i in archivo]
            archivo = [i.replace(",", ".") for i in archivo]
            archivo = [i.replace("\n", "") for i in archivo]
            diccionario={}

            for i in range(len(archivo)):
                if i == 0:
                    claves = archivo[i].split(';')
                    for j in claves:
                        diccionario[j] = []
                else:
                    linea = archivo[i].split(';')
                    for j in range(len(claves)):
                        try:
                            diccionario[claves[j]].append(float(linea[j]))
                        except ValueError:
                            diccionario[claves[j]].append(linea[j])

        return diccionario

    except FileNotFoundError:
        print(f'El archivo {ruta} no existe')
        return None

#Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el mínimo, el máximo y la media de dada columna. La función debe cumplir los siguientes requisitos:

    #La función recibirá como parámetros el diccionario con los datos de cotización y la ruta del fichero a crear.
    #El fichero generado tendrá las mismas columnas que el fichero cotizacion.csv con los mismos nombres de columnas, y tres líneas correspondientes al mínimo, máximo y media de los datos de cada columna. En la columna nombre en lugar del nombre de la empresa debe aparecer la medida calculada en esa línea (mínimo, máximo o media). Los datos deben estar separados por punto y coma.

path_final = './5_files/2.csv'

def resumen(dicc, ruta):
    del dicc['Nombre']
    
    cadena = 'Nombre'
    for i in dicc.keys():
        cadena = cadena + ';' + i

    cadena = cadena + '\nMÃ­nimo'
    for i in dicc.values():
        cadena = cadena + ';' + str(min(i))

    cadena = cadena + '\nMÃ¡ximo'
    for i in dicc.values():
        cadena = cadena + ';' + str(max(i))

    cadena = cadena + '\nMedia'
    for i in dicc.values():
        cadena = cadena + ';' + str(round(st.mean(i),2))

    with open(ruta, 'w') as f:
        f.write(cadena)
    

    


resumen(abrir(path), path_final)