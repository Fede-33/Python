# La url https://datos.madrid.es/egob/catalogo/300117-0-arrendamiento-programas.csv apunta a un fichero en formato csv con datos de los arrendamientos de viviendas de la Empresa Municipal de la Vivienda del Ayuntamiento de Madrid.

#1 Construir una función que abra un fichero con el formato anterior y devuelva una lista cuyos elementos son a su vez las listas que contienen los datos de cada línea del fichero menos la primera línea. Debe cumplir los siguientes requisitos:
    #La función recibirá como único parámetro la url del fichero.
    #Debe leer el fichero por líneas y para cada línea debe dividir la línea por el separador de campos (punto y coma) y guardar los datos en una lista.
    #Debe devolver la lista con las listas de datos obtenidas a partir de cada línea.

path = './6_files/AdjudicacionAlquilerViviendas.csv'

def abrir(ruta):
    salida = []
    with open(ruta, 'r') as f:
        salida = f.read().splitlines()
    
    salida.pop(0)

    for i in range(len(salida)):
        salida[i] = salida[i].split(';')
    
    return salida

#print(abrir(path))


#2Construir una función que reciba una lista de listas como la que devuelve la función anterior y devuelva otra lista con los nombres de los distritos contenidos en la lista. Debe cumplir los siguientes requisitos:
    #La función recibirá como único parámetro una lista de listas con las viviendas arrendadas por distrito.
    #Debe recorrer la lista de listas y para cada lista debe extraer el nombre del distrito y añadirlo a una lista con los distritos.
    #Debe devolver la lista de distritos.

def distritos(lista):
    lista_distritos=[]

    for i in range(1, len(lista)-1):
        lista_distritos.append(lista[i][0])
    
    return lista_distritos

#print(distritos(abrir(path)))


#3Construir una función que reciba una lista de listas como la que devuelve la primera función y una lista de nombres de distritos y devuelva la lista con las listas correspondientes a los distritos indicados. Debe satisfacer los siguientes requisitos:
    #La función recibirá como parámetros una lista de listas con las viviendas arrendadas por distrito y otra lista con nombres de distritos.
    #Debe recorrer la lista de viviendas arrendadas y añadir a otra lista nueva las líneas correspondientes a los distritos indicados en la segunda lista.
    #Debe devolver la nueva lista con las listas correspondientes a los distritos indicados.

nombres=['CARABANCHEL', 'CENTRO', 'CHAMARTIN', 'CHAMBERI', 'CIUDAD LINEAL']

def consulta(lista, nombres):
    salida = []

    for i in lista:
        for j in nombres:
            if j in i:
                salida.append(i)
    
    return salida

#consulta(abrir(path), nombres)


#4Construir una función que reciba una lista como la que devuelve la primera función y devuelva un diccionario cuyas claves sean los nombres de distrito y cuyos valores sean el total de viviendas arrendadas en el distrito. Debe cumplir los siguientes requisitos:
    #La función recibirá como único parámetro la lista con las viviendas arrendadas por distrito.
    #Debe recorrer la lista de listas y para cada lista extraer el nombre del distrito y el total de viviendas arrendadas en el distrito y añadir el par a un diccionario.
    #Debe devolver un diccionario con un par para cada lista de la lista, cuya clave sea el nombre del distrito y cuyo valor sea el número total de viviendas arrendadas en ese distrito.

def totales(lista):
    totales = {}

    for i in range(1, len(lista)-1):
        totales[lista[i][0]] = lista[i][1]
    
    return totales

print(totales(abrir(path)))