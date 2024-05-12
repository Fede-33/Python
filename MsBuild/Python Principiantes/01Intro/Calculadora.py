num1 = float(input('Ingrese primer número: '))
num2 = float(input('Ingrese segundo número: '))
oper = float(input('Seleccione operación: Suma(1) - Resta(2) - Producto (3) - Cociente(4) '))

if oper >= 1 and oper <= 4:
    if oper == 1:
        num3 = num1+num2
    elif oper == 2:
        num3 = num1-num2
    elif oper == 3:
        num3 = num1*num2
    elif oper == 4:
        num3 = num1/num2

    print('El resultado es:', num3)
else : print('Operación incorrecta')

