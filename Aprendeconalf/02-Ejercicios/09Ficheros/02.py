# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.


def ingreso():
    
    while True:
        try:
            num = int(input('Ingrese un múmero entero del 1 al 10: '))
            if num < 1 or num > 10:
                raise Exception
            else:
                break
        except:
            print ('\nValor incorrecto.\n')

    return num

def leertabla(n):
    while True:
        try:
            with open(f'./archivos_tablas/tabla_{n}.txt', 'r') as f: 
                print(f.read())
                break
        except:
            print ('\nEl archivo no existe.\n')
            ingreso()
    
leertabla(ingreso())