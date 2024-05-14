# Solicite al usuario que ingrese un número entero positivo y calcule su factorial. Es decir, la multiplicación de todos los valores entre 1 y ese mismo múmero.

num = -1
def fact(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res


while not num > 0:
    try:
        num = int(input('Ingrese número entero positivo: '))
        if num <= 0:
            raise ValueError
    except ValueError:
        print('Valor incorrecto.\n')

print(f'El factorial de {num} es:', fact(num))




 