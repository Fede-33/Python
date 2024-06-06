import operaciones

opr = None
n1 = operaciones.ing()
n2 = operaciones.ing()
operacion = ['+','-','x','/']

while opr == None:
    opr = input(f'Ingrese operación a realizar {operacion}: ')
    if not opr in operacion:
        opr = None
        print('Ingreso incorrecto.\n')

if opr == '+':
    result = operaciones.suma(n1, n2)
elif opr == '-':
    result = operaciones.resta(n1, n2)
elif opr == 'x':
    result = operaciones.producto(n1, n2)
else:
    result = operaciones.div(n1, n2)

print(f'\nEl resultado es {result}')