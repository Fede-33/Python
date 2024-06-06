# Realiza un programa que simule una calculadora elemental. La misma debe solicitar una operación matemática (suma, resta, multiplicación y división), dos números y mostrar el resultado. La intención es usar las funciones creadas en el punto 3 a 6.


def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def producto(num1, num2):
    return num1 * num2
def div(num1, num2):
    if num2 == 0:
        return "No se puede dividir por 0"
    else:
        return num1 / num2
def ing():
    num = None
    while num == None:
        try:
            num = float(input('Ingrese número real: '))
        except ValueError:
            print('Ingreso incorrecto.\n')
    return num

opr = None
n1 = ing()
n2 = ing()
operaciones = ['+','-','x','/']

while opr == None:
    opr = input(f'Ingrese operación a realizar {operaciones}: ')
    if not opr in operaciones:
        opr = None
        print('Ingreso incorrecto.\n')

if opr == '+':
    result = suma(n1, n2)
elif opr == '-':
    result = resta(n1, n2)
elif opr == 'x':
    result = producto(n1, n2)
else:
    result = div(n1, n2)

print(f'\nEl resultado es {result}')


