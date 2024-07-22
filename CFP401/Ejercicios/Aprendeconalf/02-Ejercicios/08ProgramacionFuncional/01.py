descuento = lambda precio, desc : (precio - (desc * precio / 100))  
mas_iva = lambda precio, iva : (precio + (iva * precio / 100))

def cierre (carr, funcion):
    valores = map(funcion, carr.keys(), carr.values())
    return sum(valores)


carrito = {1000:20, 500:10, 100:1}

print (cierre(carrito, descuento))
print (cierre(carrito, mas_iva))


#Otra forma:


def descuento(precio, desc):
    return precio - precio * desc / 100
    
def mas_iva(precio, iva):
    return precio + precio * iva / 100

def cierre(carr, funcion):
    total = 0
    for precio, porcentaje in carr.items():
        total += funcion(precio, porcentaje)
    return total

print('El precio de la compra tras aplicar los descuentos es: ', cierre({1000:20, 500:10, 100:1}, descuento))
print('El precio de la compra tras aplicar el IVA es: ', cierre({1000:20, 500:10, 100:1}, mas_iva))