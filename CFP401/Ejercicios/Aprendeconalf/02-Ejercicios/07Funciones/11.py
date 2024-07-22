#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def palabras(texto):
    texto = texto.split()
    dicc = {}
    for i in texto:
        if i in dicc:
            dicc[i] += 1
        else:
            dicc[i] = 1
    return dicc

def mas_repetida(palabra):
    max_word = ''
    max_freq = 0
    for word, freq in palabra.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(palabras(text))
print(mas_repetida(palabras(text)))