# Definir una función que reciba una lista de facturas, un NIF y un mes, y devuelva un diccionario con el número de facturas emitidas a ese NIF en el mes indicado y el total facturado en ese mes. La función debe cumplir los siguientes requisitos:

    #Los parámetros de entrada serán una lista de facturas, una cadena con un NIF y otra cadena con el mes.
    #Cada factura se representarán mediante un diccionario con las claves nif (NIF del cliente), mes (mes de emisión de la factura), cantidad (cantidad facturada sin IVA), iva (porcentaje de IVA a aplicar).
    #Se debe crear una lista con el total de cada factura (una vez aplicado el IVA) para el NIF y el mes indicados utilizando programación funcional o comprensión de listas.
    #La función debe devolver un diccionario con el número de facturas y el total facturado al NIF en el mes indicado.

def cuenta_facturas(lista, nif, mes):
    diccionario = {
        'cantidad': 0,
        'total': 0
        }
    
    for i in lista:
        if i['NIF'] == nif and i['mes'] == mes:
            diccionario['cantidad'] +=1
            diccionario['total'] += (i['cant'] + i['cant']*i['IVA']/100)
    
    return diccionario

facturas = [
    {
    'NIF': 'a1',
    'mes': 'enero',
    'cant': 100,
    'IVA': 20},
    {
    'NIF': 'a1',
    'mes': 'enero',
    'cant': 1000,
    'IVA': 10},
    {
    'NIF': 'a2',
    'mes': 'febrero',
    'cant': 100,
    'IVA': 10},
    {
    'NIF': 'a2',
    'mes': 'enero',
    'cant': 1000,
    'IVA': 20}
]

print(cuenta_facturas(facturas, 'a1', 'enero'))

