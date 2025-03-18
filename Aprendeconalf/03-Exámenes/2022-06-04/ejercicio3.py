# Realizar un programa que analice el pasaje Lorem ipsum y realice las siguientes operaciones:


li = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    #1 Crear un diccionario con la frecuencia de cada carácter sin tener en cuenta el espacio.

diccionario = {}

for i in li:
    if i != ' ':
        if i in diccionario.keys():
            diccionario[i] += 1
        else:
            diccionario[i] = 1

    #2 Muestre por pantalla el carácter que más se repite.

repe = max(diccionario.values())
for i in diccionario.keys():
    if diccionario[i] == repe:
        caract = i
        print(f'Caracter más repetido: {caract}')

    #3 Muestre por pantalla las palabras que contienen el carácter más repetido y su frecuencia por palabra.

lista = li.split(' ')
diccpal = {}

for i in lista:
    if caract in i:
        diccpal[i] = i.count(caract)

print(f'Las palabras con el caracter más repetido son:\n {diccpal}')