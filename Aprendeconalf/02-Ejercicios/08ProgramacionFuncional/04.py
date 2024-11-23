# Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.

def positivo (num):
    if num >= 0:
        return True
    else :
        return False
            
def func_bool (funcion, nums):
    lista_dos = []
    for i in nums:
        lista_dos.append(funcion(i))
    return lista_dos

lista = [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]

lista_bool = func_bool (positivo, lista)

for i in range(len(lista)):
    print (lista[i], ' : ', lista_bool[i]) 
    