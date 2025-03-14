# Construir un programa que evalúe operaciones aritméticas sencillas (sumas, restas, productos, cocientes y potencias) introducidas por el usuario. El programa preguntará por la operación a realizar y el usuario tecleará por pantalla la operación con el siguiente formato:

# operando1 operador operando2

# Después el programa debe mostrar por pantalla el resultado de la operación con el siguiente formato:

# operando1 operador operando2 = resultado

# El programa debe preguntar al usuario hasta que este introduzca la palabra “salir”. También mostrará un mensaje de error si el usuario introduce un número de valores distinto de 3 y si introduce un operador no válido.

ingreso=''
operadores=['+', '-', '*', '/', '**', '//']

while ingreso != 's'.upper():
    ingreso = input(f'''Ingrese "Operando1 Operador Operando2" Los operadores admitidos son:
        \t {operadores} \n\t''').upper()

    try: 
        op_1 = ingreso.split(' ')[0]
        opr = ingreso.split(' ')[1]
        op_2 = ingreso.split(' ')[2]

        if opr == '+':
            res = float(op_1) + float(op_2)
        if opr == '-':    
            res = float(op_1) - float(op_2)
        if opr == '*':    
            res = float(op_1) * float(op_2)
        if opr == '/':    
            res = float(op_1) / float(op_2)
        if opr == '**':    
            res = float(op_1) ** float(op_2)
        if opr == '//':    
            res = float(op_1) ** (1/float(op_2))


        print(f'\n\t{op_1} {opr} {op_2} = {res} \n')
    
    except:
        if ingreso != 's'.upper():
            print('\n\tValores incorrectos.\n')

print('Adios')