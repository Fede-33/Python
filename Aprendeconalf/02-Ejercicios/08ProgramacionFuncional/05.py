# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

def contarfrase (cadena):
    diccionario = {}
    for i in cadena:
        diccionario [i] = len(i)
    return diccionario

frase = input('Ingrese una frase: ').split()

print(contarfrase(frase))

