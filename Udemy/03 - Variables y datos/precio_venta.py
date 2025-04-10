# Ingresado el valor de un producto, hallar el IGV (18%) y el precio de venta.

valor = float(input('Ingrese valor del producto: '))

igv = valor * 0.18
precio = valor + igv

print(f'{'-'*30}\nValor del producto: ${valor:.2f}\nIGV: ${igv:.2f}\nPrecio final: ${precio:.2f}\n{'-'*30}') # el método :.2f sirve para formatear la salida con solo 2 decimales redondeado.