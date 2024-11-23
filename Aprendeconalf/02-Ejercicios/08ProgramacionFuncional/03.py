# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

def aplicar (funcion, nums):
    for i in nums:
        print (funcion(i))

def masuno (num):
    return num + 1

lista = (0,1,2,3,4,5,6,7,8,9)

aplicar(masuno, lista)
