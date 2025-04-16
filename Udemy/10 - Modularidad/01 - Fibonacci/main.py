from secuencia import fibo, lista_fibo

while True:
    try:
        num = int(input('Ingrese cantidad de valores: '))
        if num < 0:
            raise ValueError
        else:
            break
    except ValueError:
        print('Sólo números enteros positivos.\n')

fibo(num)
print('')
print(lista_fibo(num))