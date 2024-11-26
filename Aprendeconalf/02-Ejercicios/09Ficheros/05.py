# Escribir un programa que abra el fichero con información sobre el PIB per cápita, pregunte por el nombre de un país y muestre el PIB per cápita de ese país de todos los años disponibles.

def ingreso():

    while True:
        try:
            clave = input('Ingrese nombre del país (al menos tres letras): ')
            if len(list(clave)) < 3:
                raise ValueError
            else:
                print('')
                break
        except:
            print('\nInténtelo otra vez.\n')
    
    return clave

def buscarpbi(clave):
    resp = False
    with open(f'./archivo_pbi/GDP_by_Country_1999-2022.csv', 'r') as f: 
        datos = f.readlines()
        encabezado = datos[0].split(',')
        for i in range(1,len(datos)):
            linea = datos[i].split(',')
            if clave.lower() in linea[0].lower():
                resp = True
                print(f'PBI de {linea[0]}:')
                for j in range(1,len(linea)):
                    print(f'{int(encabezado[j])} : {linea[j]}')

    if resp == False:
        print('No se halló el país indicado. Inténtelo otra vez.')
        buscarpbi(ingreso())

buscarpbi(ingreso())


