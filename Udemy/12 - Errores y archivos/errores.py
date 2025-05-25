while True:
    try:
        n = int(input('Ingrese 1 para continuar o 2 para salir: '))
        if n != 1 and n != 2:
            raise ValueError
        elif n == 2:
            print('Adios')
            break
    except ValueError:
        print ('Ingreso incorrecto')
    else:
        print('Continuar')


while True:
    try:
        n = int(input('Ingrese 1 para continuar o 2 para salir: '))
        if n != 1 and n != 2:
            raise Exception ('Opción incorrecta')
        if n == 2:
            print('Adios')
            break
    except Exception as error:
        print ('Ocurrió un error: ', type(error).__name__)
    else:
        print('Continuar')

while True:
    try:
        n = int(input('Ingrese 1 para realizar una división o 2 para salir: '))
        if n != 1 and n != 2:
            raise Exception ('Opción incorrecta')
        if n == 2:
            print('Adios')
            break
        a = int(input('Ingrese dividendo: '))
        b = int(input('Ingrese divisor: '))
        print(f'\nLa división entre {a}/{b} es: {a/b}')
    except ValueError:
        print('Ingrese un número entero')
    except ZeroDivisionError:
        print('No se puede dividir por 0')        
    except Exception as error:
        print ('Ocurrió un error: ', error)


class OperadorExcepcion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

def dividir(a, b):
    if b == 0:
        raise OperadorExcepcion('Error: No se puede dividir por 0')
    else:
        return a / b

dividir(4,0)
