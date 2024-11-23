#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

#Plátano 1.35
#Manzana 0.80
#Pera 0.85
#Naranja 0.70

frutas = {
    'Plátano' : 1.35,
    'Manzana' : 0.80,
    'Pera' : 0.85,
    'Naranja' : 0.70
}

fruta = input('Ingrese la fruta: ').capitalize()

if fruta in frutas:
    cant = int(input('Ingrese cantidad de Kg: '))
    print(f'El precio es ${cant * frutas[fruta]}.')
else:
    print(f'No hay {fruta.lower()} en existencia.')
