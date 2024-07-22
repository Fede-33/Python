#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

diccionario = {}
continuar = 'S'
c=0

while continuar == 'S':
    ingreso = input('Ingrese palabra:traducción: ').split(':')
    print(ingreso)
    diccionario[ingreso[0]] = ingreso[1]
    print(diccionario)
    continuar = input('Desea continuar (S/N)').upper()

frase = input('Ingrese la frase a traducir: ').split(' ')

for i in frase:
    for j in diccionario:
        if i == j:
            frase[c] = diccionario[j]
    c += 1

print (f'La traducción es:\n{" ".join(frase)}')