# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

#Lista de la compra 	
#Artículo 1 	Precio
#Artículo 2 	Precio
#Artículo 3 	Precio
#… 	…
#Total 	Coste

carrito ={}
continuar = 'S'
total = 0

while continuar == 'S':
    articulo = input('Ingrese nombre del artículo: ')
    carrito[articulo] = float(input(f'Ingrese precio de {articulo}: '))
    continuar = input('¿Desea continuar? (S/N) ').upper()

print('Lista de compra')
for i in carrito:
    print(f'{i}   ${carrito[i]}')
    total += carrito[i]

print(f'Total   ${total}')
