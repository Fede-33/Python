# Escribir una función que cuente las palabras que hay en una frase y las devuelva dentro de un diccionario. También tiene que devolver una lista con las palabras que aparecen más de una vez. Por ejemplo si se le pasa la frase: La caracola está enterrada al lado de otra caracola de color la función debe devolver el diccionario y la lista siguientes:

def contar(cadena):
    cadena = cadena.split(' ')
    diccionario = {}
    lista = []
    for i in cadena:
        diccionario[i] = cadena.count(i)
        if cadena.count(i) > 1 and i not in lista:
            lista.append(i)

    return diccionario, lista

frase = 'La caracola está enterrada al lado de otra caracola de color'

imprime = (contar(frase))

for i in imprime:
    print(i)