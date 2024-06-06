# Crear una función que dado dos números reales, realice su resta. 

def resta(num1, num2):
    return num1 - num2

n1 = float(input('Ingrese número real: '))
n2 = float(input('Ingrese número real: '))

print(f'La resta de {n1} y {n2} da como resultado {resta(n1,n2)}')