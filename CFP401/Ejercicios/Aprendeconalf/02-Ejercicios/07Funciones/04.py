#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def iva (precio, val = 21):
    return precio + (precio * val / 100)

factura = int(input('Ingrese monto de factura: '))
impuesto = input('Ingrese valor de IVA: ')
if impuesto == '':
    resultado = iva(factura)
else:
    impuesto = int(impuesto)
    resultado = iva(factura, impuesto)


print(f'El monto a pagar es de ${resultado}')