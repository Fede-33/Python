# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

frase = ''

while frase == '':
    frase = input('Ingrese lo que se le ocurra: ')
    
for i in range(10):
    print(frase)