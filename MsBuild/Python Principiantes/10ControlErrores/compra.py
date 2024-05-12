#Establezca una cantidad de dinero arbitraría en la cuenta del usuario. Pídale que ingrese el valor de un producto y la cantidad deseada. Calcule el monto a abonar y decuéntelo de su saldo. Si el usuario agota su saldo, genere una excepción que devuelva un mensaje y deshaga la compra. Pregunte al usuario si quiere continuar la compra. Agregue control sobre los ingresos del usuario para evitar errores de tipo de dato:

saldo = 1000

while saldo > 0:
    preg = ''
    print(f'\nUsted tiene ${saldo}\n')
    try:
        precio = float(input('Ingrese valor unitario del producto: '))
        cant = int(input('Ingrese cantidad de unidades: '))
        saldo = saldo - (precio * cant)
        if saldo < 0:
            raise RuntimeError
        print(f'\nCompra realizada. Usted tiene ${saldo}\n')
    except ValueError:
        print('Valores incorrectos.\n')
    except RuntimeError:
        print ('Saldo Insuficiente para realizar la compra.\n')
        saldo = saldo + (precio * cant)

    while saldo > 0 and preg != 'n' and preg != 's':
        preg = input('¿Desea continuar la compra? (s/n) ').lower()
    if preg == 'n':
        print(f'Saldo restante ${saldo}')
        break
    


print('\nGracias por su compra.')
