#Los productos en oferta de una tienda de informática se guardan una cadena como la de más abajo, donde cada línea (separadas por el carácter de cambio de línea ‘\n’) contiene el nombre del producto, el número de unidades en stock, el precio (en €) y el descuento que tiene (en porcentaje), separados por punto y coma.

oferta = 'disco duro 500Gb;200;25;15\nmemoria ram 16Gb;500;30;20\nratón inalámbrico;800;12;10\ntarjeta wifi;150;20;12'

# Construir un programa que genere, a partir de la cadena anterior, un diccionario como el de más abajo, donde cada par corresponda un producto, siendo la clave el nombre del producto y el valor una lista con el resto de la información del producto.

diccionario = {}

for i in oferta.split('\n'):
    valores = []
    for j in range(len(i.split(';'))):
        if j == 0:
            clave = i.split(';')[j]
        else:
            valores.append(i.split(';')[j])
    diccionario[clave] = valores

# Después el programa debe recorrer el diccionario y mostrar por pantalla un listado con los nombres de todos los productos en oferta y su precio final tras aplicar el descuento.

for i in diccionario:
    precio = float(diccionario[i][1])*(1-float(diccionario[i][2])/100)
    print(f'El valor con descuento del producto {i}, es de: {precio}')