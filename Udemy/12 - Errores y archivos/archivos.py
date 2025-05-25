from io import open
from os import path

def escribir_archivo(nombre, texto):
    archivo = open(nombre, 'w')
    archivo.write(texto)
    archivo.close()
    return 'Archivo creado.\n'

def leer_archivo(nombre):
    archivo = open(nombre, 'r')
    texto = archivo.read()
    archivo.close()
    return f'\n{nombre}:\n{texto}\n'
    
def actualizar_archivo(nombre, texto):
    archivo = open(nombre, 'a')
    archivo.write(texto)
    archivo.close()
    return'Archivo actualizado.\n'

def modificar_archivo(nombre):
    archivo = open(nombre, 'r+')
    print(f'\n{nombre}:\n{archivo.read()}\n')
    texto = input('Ingrese nuevo texto: ')
    archivo.seek(0)
    archivo.write(texto)
    archivo.close()
    return'Archivo modificado.\n'

def existe_archivo(nombre):
    if path.isfile(nombre):
        return True
    else:
        return False





