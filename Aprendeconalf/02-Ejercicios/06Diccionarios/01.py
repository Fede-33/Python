#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

diccionario = {
    'Euro':'€', 
    'Dollar':'$', 
    'Yen':'¥'
}

divisa = input('Ingrese la divisa deseada: ').capitalize()

if divisa in diccionario:
    print (f'El símbolo de {divisa} es: {diccionario[divisa]}.')
else:
    print (f'{divisa} no es una divisa válida o no se encuentra en el listado.')


# Otra forma de resolver:

print(diccionario.get(divisa, 'No se encuentra'))
#El método get permite ingresar un argumento que se busca, y separado por comas, devolver un mensaje si el argumento no está.