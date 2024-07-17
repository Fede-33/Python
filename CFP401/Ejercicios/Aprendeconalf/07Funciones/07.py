# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def cuadrat (list):
    retorno = []
    for i in list:
        retorno.append(i**2)
    return retorno

lista = [1, 2, 3, 4, 5]

print(cuadrat(lista))

