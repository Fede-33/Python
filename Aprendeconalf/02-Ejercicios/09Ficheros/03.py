# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

def ingreso():
    
    while True:
        try:
            numa = int(input('Ingrese primer número entero del 1 al 10: '))
            numb = int(input('Ingrese segundo múmero entero del 1 al 10: '))
            if numa not in range(1,11):
                raise ValueError('Primer')
            elif numb not in range(1,11):
                raise ValueError('Segundo')
            else:
                break
        except ValueError as e:
            print (f'\n{e} valor incorrecto.\n ')
    
    return numa, numb

def leertabla(tupla):
    n, m = tupla
        
    while True:
        try:
            with open(f'./archivos_tablas/tabla_{n}.txt', 'r') as f: 
                print(f.readlines()[m+2])
                break
        except:
            print ('\nEl archivo no existe.\n')
            ingreso()
    
leertabla(ingreso())