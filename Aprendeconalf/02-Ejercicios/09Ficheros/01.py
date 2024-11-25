# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

def ingreso():
    
    while True:
        try:
            num = int(input('Ingrese un múmero entero del 1 al 10: '))
            if num < 1 or num > 10:
                raise Exception
            else:
                break
        except:
            print ('\nInténtelo otra vez.\n')

    return num

def guardatabla(n):
    
    with open(f'tabla_{n}.txt', 'w') as f: 
        f.write(f'Tabla del {n}\n')
    
    with open (f'tabla_{n}.txt', 'a') as f:    
        for i in range(11):
            f.write(f'\n{n} X {i} = {i*n}')


guardatabla(ingreso())