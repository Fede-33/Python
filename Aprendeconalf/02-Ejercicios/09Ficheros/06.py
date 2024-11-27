#Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.csv donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.

import sys
import os

def menu():
    while True:
        try:
            opc = int(input ('AGENDA TELEFÓNICA:\n\n\t1 - Consultar teléfono.\n\t2 - Anadir teléfono.\n\t3 - Eliminar teléfono.\n\t4 - Salir.\n\n\tIngrese opción: '))
            if opc not in range (1, 5):
                raise ValueError('\nOpción incorrecta. Inténtelo otra vez\n')
            else:
                break
        except ValueError as e:
            print(e)
    
    return opc

def operador(n):
    if n == 1:
        consultar()
    elif n == 2:
        agregar()
    elif n == 3:
        eliminar()
    else :
        print('\n\tFin del programa.\n')
        sys.exit()

def consultar():
    consulta = input('\nIngrese nombre o número a consultar: ')
    with open('./archivo_tel/listin.csv', 'r') as f:
        datos = f.readlines()
        respuesta = False
        for i in range(1, len(datos)):
            linea = datos[i].split(',')
            nombre = linea[0]
            tel = linea[1].split("\n")[0]
            if consulta.lower() == nombre.lower():
                respuesta = f'el número de {consulta} es: {tel}\n'
            elif consulta == tel:
                respuesta = f'el número {consulta} corresponde a {nombre}\n'

    if respuesta :
        print(f'\n{respuesta}')
    else :
        print(f'\n{consulta} no se encuentra en la agenda.\n')

def agregar():
    while True:
        try:
            nombre = input('\nIngrese nombre: ')
            if not nombre:
                raise Exception('\nEl nombre no puede estar vacío.')
            tel = input('Ingrese teléfono (diez caracteres): ')
            try:
                tel = int(tel)
                if len(str(tel)) != 10 :
                    raise ValueError
                else:
                    break
            except ValueError:
                print('\nNúmero incorrecto.')
        except Exception as e:
            print(e)
        
    with open('./archivo_tel/listin.csv', 'a') as f:
        f.write(f'{nombre},{tel}\n')
        print('\n\tTeléfono agregado.\n')

def eliminar():
    deletear = input('\nIngrese nombre o número a eliminar: ')
    respaldo = ['nombre,tel']
    with open('./archivo_tel/listin.csv', 'r') as f:
        datos = f.readlines()
        respuesta = False
        for i in range(1, len(datos)):
            linea = datos[i].split(',')
            nombre = linea[0]
            tel = linea[1].split("\n")[0]
            if deletear.lower() == nombre.lower() or deletear == tel:
                respuesta = f'el registro de {linea[0]} fue eliminado.\n'
            else:
                respaldo.append(f'{nombre},{tel}')
    
    if respuesta :
        os.remove('./archivo_tel/listin.csv')
        with open('./archivo_tel/listin.csv', 'w') as f:
            for i in respaldo:
                f.write(f'{i}\n')
        print(f'\n{respuesta}')
        
    else :
        print(f'\n{deletear} no se encuentra en la agenda.\n')

# EJECUCIÓN:
if not os.path.isfile('./archivo_tel/listin.csv'):
    with open('./archivo_tel/listin.csv', 'w') as f:
        f.write('nombre,tel\n')

while True:
    operador(menu())
