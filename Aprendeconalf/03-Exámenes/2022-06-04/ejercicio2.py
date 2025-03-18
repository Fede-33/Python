# Realizar un programa que simule la operativa de una cuenta bancaria. El programa debe preguntar al usuario si desea realizar un ingreso o un reintegro hasta que el usuario decida terminar el programa.
# Si el usuario selecciona la opción de ingreso, debe preguntarle por la cantidad a ingresar e incrementar el saldo en esa cantidad.
# Si el usuario selecciona la opción de reintegro deberá preguntarle por la cantidad a sacar y sustraerla del saldo, siempre y cuando haya saldo suficiente. Si no hubiese saldo suficiente avisará al usuario y no realizará el reintegro.
# Las cantidades de las operaciones deben guardarse en una sola lista (positivos para ingresos y negativos para reintegros), y después de cada operación debe mostrarse el saldo por pantalla.
# Cuando el usuario ya no quiera hacer más operaciones, a partir de la lista de operaciones se deben crear dos listas más, una para los ingresos y otra para los reintegros y deben mostrarse por pantalla.

saldo = 0
operaciones = []

def monto():
    try:
        valor = float(input('Ingrese monto positivo: '))
        if valor <= 0:
            valor = 0
            raise ValueError
    except ValueError:
        print('Monto incorrecto.\n')
    
    return valor

def ingreso(saldo):
    lista = []
    valor = monto()
    
    saldo += valor
    lista.append(valor)

    return saldo, lista

def reintegro(saldo):
    lista = []
    valor = monto()
    
    if saldo >= valor:
        saldo -= valor
        lista.append(0-valor)
    else:
        print('Saldo insuficiente\n')

    return saldo, lista

def listar(operaciones):
    positivos = []
    negativos = []

    for i in operaciones:
        if i > 0:
            positivos.append(i)
        if i < 0:
            negativos.append(i)
    
    print(f'\nIngresos: {positivos}\nReintegros: {negativos}')

while True:
    print('1-Ingreso\t2-Reintegro')
    opc = input('Ingrese opción (Otra para finalizar):\n')
    if opc == '1':
        saldo, lista = ingreso(saldo)
        operaciones.extend(lista)
        print(f'Saldo: {saldo}\n')
    elif opc == '2':
        saldo, lista = reintegro(saldo)
        operaciones.extend(lista)
        print(f'Saldo: {saldo}\n')
    else:
        listar(operaciones)
        print(f'Saldo: {saldo}')
        print('Adios\n')
        break