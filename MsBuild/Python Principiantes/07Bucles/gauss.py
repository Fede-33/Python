#Ingresando un número entero positivo, se calcule la sumatoria de todos los valores enteros positivos hasta ese mismo número. (Fórmula de Gauss)

num = -1
def gauss(n):
    res = 0
    for i in range(1, n+1):
         res += i
    return res


while not num > 0:
    try:
        num = int(input('Ingrese número entero positivo: '))
        if num <= 0:
            raise ValueError
    except ValueError:
        print('Valor incorrecto.\n')

print(f'El factorial de {num} es:', gauss(num))