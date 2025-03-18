# Escribir un programa que elimine de una lista dada todos los elementos repetidos y muestre por pantalla los elementos de la lista sin repeticiones.



lista = [1,2,4,4,3,4,5,9,9,7,7,7,7,5,6,7,8,9,]

for i in lista:
    while lista.count(i) > 1:
        lista.remove(i)
 
print(lista)