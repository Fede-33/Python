#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

facturas = {}
op = 1
cobrado = 0

while op != 3:
    try:
        op = int(input('\nIngrese operación:\n1-Añadir factura\n2-Pagar factura\n3-Terminar\n'))
        if op < 1 or op > 3:
            raise ValueError
    except ValueError:
        print('\nOperación incorrecta\n')
    if op == 1:
        try:
            num = int(input('Ingrese número de factura: '))
            precio = float(input('Ingrese costo: $'))
            facturas[num] = precio
        except:
            print('\nIngreso incorrecto\n')
    elif op == 2:
        try:
            elim = int(input('Ingrese número de factura a pagar: '))
            cobrado += facturas[elim]
            facturas.pop(elim)
        except:
            print('\nIngreso incorrecto\n')
    else:
        print('Fin de las operaciones.')
    
    print(f'\nCantidad cobrada: ${cobrado}')
    print(f'Cantidad por cobrar: ${sum(facturas.values())}\n')