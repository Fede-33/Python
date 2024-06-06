# Dada la siguiente lista de notas obtenidas: notas_obtenidas = [6, 8, 5, 4 , 10, 9, 9, 9] identifique cual es la mayor, muestre el resultado por pantalla. Nota: no es posible utilizar funciones o primitivas de Python. Sugerencia: pruebe iterar toda la lista e ir determinando en cada paso cual es la nota mayor.

notas_obtenidas = [6, 8, 5, 4, 10, 9, 9, 9]
mayor = 0

for i in notas_obtenidas:
    if i > mayor:
        mayor = i    

print(mayor)