#Dadas dos listas de números del mismo tamaño x e y, construir las siguientes funciones:

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [20, 18, 12, 10, 9, 9]

    #1 Una función para calcular la media de una lista de números.
    
def media(lista):
    suma = 0
    for i in lista:
        suma += i
    
    return suma / len(lista)

    #2 Una función para calcular la varianza de una lista de números.

def varianza(lista):
    suma = 0
    for i in lista:
        suma += i ** 2
    
    return suma / len(lista) - media(lista) ** 2

    #3 Una función para calcular la covarianza de dos listas de números.
    
def covarianza(l_1, l_2):
    suma = 0
    for i in range(len(l_1)):
        suma += l_1[i] * l_2[i]

    return suma / len(l_1) - media(l_1) * media(l_2)    

    #4 Una función para calcular los coeficientes de la recta de regresión de y sobre x.
    
def regresion(l_1, l_2):
    a = covarianza(l_1, l_2) / varianza(l_1)
    b = media(l_2) - a * media(l_1)

    return a,b    
    
    #5 Una función que devuelva el diagrama de dispersión y la recta de regresión como la que se muestra en el siguiente ejemplo:

def grafica(l_1, l_2):
    fig, ax = plt.subplots()
    ax.scatter(l_1, l_2)
    a,b = regresion(l_1, l_2)
    ax.plot([min(l_1), max(l_1)], [a * min(l_1) + b, a * max(l_1) + b], color='green')
    plt.show()

print(grafica(x, y))