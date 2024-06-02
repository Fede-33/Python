# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

lista = []
cont = 0
varianza = 0

lista = input('Ingrese una muestra de números separados por coma: ')

lista = lista.split(',')

for i in range(len(lista)):
    lista[i] = float(lista[i])

for i in lista:
    cont += i
media = cont / len(lista)

print(f'La media entre: \n{lista}\nes {media}')

for i in lista:
    varianza += (i - media)**2

desviacion = (varianza / len(lista))**(1/2)

print(f'Y la desviación típica es: {desviacion}')