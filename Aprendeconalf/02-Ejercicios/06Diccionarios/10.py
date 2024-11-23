#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: 

# (1) Añadir cliente: Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# (2) Eliminar cliente: Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# (3) Mostrar cliente: Preguntar por el NIF del cliente y mostrar sus datos.
# (4) Listar todos los clientes: Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# (5) Listar clientes preferentes: Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# (6) Terminar: Terminar el programa.


clientes = {}
op = 1

while op != 6:
    try:
        op = int(input('\n1- Añadir cliente\n2- Eliminar cliente\n3- Mostrar cliente\n4- Listar clientes\n5- Listar clientes preferentes\n6- Finalizar\nIngrese opción: '))
        if op < 1 or op > 6:
            raise ValueError
    except:
        print('\nOpción incorrecta.\n')
    
    if op == 1:
        try:
            nif = int(input('\nIngrese NIF: '))
            if nif in clientes:
                raise RuntimeError
            cli={}
            cli['nombre'] = input('Ingrese nombre: ')
            cli['direccion'] = input('Ingrese dirección: ')
            cli['tel'] = int(input('ingrese teléfono: '))
            cli['correo'] = input('Ingrese correo: ')
            prefe = input('Es cliente preferente: (S/N)').upper()
            if prefe == 'S':
                cli['pref'] = True
            elif prefe == 'N':
                cli['pref'] = False
            else:
                raise ValueError
            clientes[nif] = cli
        except ValueError:
            print('\nIngreso incorrecto.\n')
        except RuntimeError:
            print('\nEl cliente ya existe\n')
    elif op == 2:
        try:
            nif = int(input('\nIngrese NIF: '))
            if not nif in clientes:
                raise RuntimeError
            clientes.pop(nif)
        except ValueError:
            print('\nIngreso incorrecto.\n')
        except RuntimeError:
            print('\nEl cliente no existe.\n')
    elif op == 3:
        try:
            nif = int(input('\nIngrese NIF: '))
            if not nif in clientes:
                raise RuntimeError
            if clientes[nif]['pref'] == True:
                prefe = 'Sí'
            else:
                prefe = 'No'
            print(f"\nCliente nro: {nif}\n Nombre:{clientes[nif]['nombre']}\n Dirección:{clientes[nif]['direccion']}\n Teléfono:{clientes[nif]['tel']}\n Preferente:{prefe}\n")
        except ValueError:
            print('\nIngreso incorrecto.\n')
        except RuntimeError:
            print('\nEl cliente no existe.\n')
    elif op == 4:
        print('\nLista de clientes:')
        for i in clientes:
            print(f" Nro: {i} Nombre: {clientes[i]['nombre']}")
    elif op == 5:
        print('\nLista de clientes preferentes:')
        for i in clientes:
            if clientes[i]['pref'] == True:
                print(f" Nro: {i} Nombre: {clientes[i]['nombre']}")
    elif op == 6:
        print('\nFin del programa.')
