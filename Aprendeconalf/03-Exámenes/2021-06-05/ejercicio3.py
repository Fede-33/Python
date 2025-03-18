# El siguiente diccionario contiene pares formados por números de teléfonos y propietarios:

diccionario = {'919654665':'Pedro', '917489210': 'Luis', '623543213':'Carmen', '674833721':'Luis'}

# Crear un programa que construya un diccionario con la misma información, pero tomando como claves los nombres de los usuarios y como valores los teléfonos. Como un usuario puede tener dos teléfonos, uno móvil y uno fijo, los teléfonos deben agruparse a su vez en un diccionario cuyos elementos tendrán clave “movil” o “fijo” según el teléfono empiece por 6 o no. Por ejemplo, a partir del diccionario anterior debe construirse el siguiente diccionario:

telefonos = {}

for i in diccionario.values():
    telefonos[i] = {}

for clave, valor in diccionario.items():

    if clave.startswith('6'):
        telefonos[valor]['movil'] = clave
    else:
        telefonos[valor]['fijo'] = clave

telefonos = dict(sorted(telefonos.items()))

for i in telefonos:
    print (f'Telefonos de {i}:')
    for j in telefonos[i]:
        print(f'\t{j} : {telefonos[i][j]}')