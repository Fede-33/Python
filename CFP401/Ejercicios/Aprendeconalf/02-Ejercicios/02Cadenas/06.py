# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

text = input('Ingrese una frase: ')
voc = input('Ingrese una vocal: ')

print(text.replace(voc, voc.upper()))