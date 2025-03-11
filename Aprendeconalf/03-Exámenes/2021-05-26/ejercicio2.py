# Escribir una función que, dado un número x, genere una matriz cuadrada (x*x elementos) con el resultado de sus tablas de multiplicar desde 0 hasta x. El resultado debe guardarse en un fichero llamado tabla-X.txt donde X es el número introducido por el usuario.

def matriz (n):

    f= open(f'./2_files/tabla-{n}.txt', 'w')

    for i in range(n+1):
        for j in range(n+1):
            f.write(f'{i*j}\t')
        f.write('\n')

    f.close()

matriz(5)

# Escribir otra función que, dado un número x, acceda al fichero de la tabla correspondiente y muestre la tabla por pantalla. En caso de que la tabla no exista deberá controlar la excepción para mostrar un mensaje de aviso al usuario.

def consulta (n):

    try:
        f= open(f'./2_files/tabla-{n}.txt', 'r')
        lineas = f.readlines()
        for i in lineas:
            print(i)
    except FileNotFoundError:
        print('La tabla no existe')

consulta(6)        