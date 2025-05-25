from archivos import *

while True:
    try: 
        opc = int(input('1- Crear y escribir.\n2- Actualizar.\n3- Leer.\n4- Modificar.\n5- Eliminar contenido.\n6- Salir\nIngrese opción: '))
        if opc < 1 or opc > 6:
            raise Exception ('Opción incorrecta.')
        elif opc != 6:
            nombre = input('Ingrese nombre del archivo: ')
            if existe_archivo(nombre):
                if opc == 1:
                    continuar = input('El archivo ya existe, se reescribirá (Ingrese S para continuar): ').upper()
                    if continuar == 'S':
                        texto = input('Ingrese texto: ')
                        print(escribir_archivo(nombre, texto))
                    else:
                        print ('Operación cancelada.')
                elif opc == 2:
                    texto = input('Ingrese texto: ')
                    print(actualizar_archivo(nombre, texto))
                elif opc == 3:
                    print(leer_archivo(nombre))
                elif opc == 4:
                    print(modificar_archivo(nombre))
                else:
                    print(escribir_archivo(nombre,''))
                    print('Contenido borrado.\n')
            else:
                print(f'\nArchivo no encontrado.\n')
        else:
            print('Adios.')
            break
    except Exception as error:
        if type(error).__name__ == 'ValueError':
            print(f'\nOpción incorrecta.\n')
        else:
            print (f'\n{error}\n')


