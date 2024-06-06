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