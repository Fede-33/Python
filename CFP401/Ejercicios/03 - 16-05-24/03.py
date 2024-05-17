#  Crear una función que dado dos números reales, realice su suma. Tener en cuenta que este tipo de funciones debe retornar un resultado. La última instrucción de la función debe ser un return resultado por ejemplo.

def suma(num1, num2):
    return num1 + num2

n1 = int(input('Ingrese número entero: '))
n2 = int(input('Ingrese número entero: '))

print(f'La suma de {n1} y {n2} da como resultado {suma(n1,n2)}')