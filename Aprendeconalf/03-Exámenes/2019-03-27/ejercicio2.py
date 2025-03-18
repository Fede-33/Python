#Escribir un programa que realice la devolución de una cantidad dada por el usuario en monedas. El programa debe cumplir los siguientes requisitos:

# Solo se disponen de tres tipos de monedas: 5, 2 y 1 €. Crear una lista que contenga estos tres tipos de moneda y usar la lista en la solución.
# El programa debe preguntar al usuario por una cantidad entera de euros.
# El programa debe mostrar por pantalla el mínimo número de monedas necesarias para sumar la cantidad introducida por el usuario y cuántas monedas de cada tipo se necesitan para ello. El número de monedas de cada tipo debe guardarse en otra lista.
# El programa debe guardarse dentro de la carpeta respuestas con el nombre ejercicio2.py.
# Cuando el programa esté terminado, añadir el fichero ejercicio2.py a la zona de intercambio temporal y hacer un commit con el mensaje “Añadida respuesta ejercicio 2”.

moneda = [5, 2, 1]
cantidad = []

ingreso = int(input('Ingrese una cantidad entera de Euros: ' ))

for i in moneda:
    cantidad.append(int(ingreso / i))
    ingreso = ingreso % i

print('Se necesitan:')
for i in range(3):
    print(f'{cantidad[i]} monedas de {moneda[i]}' )
