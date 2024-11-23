# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

from math import sin, cos, tan, exp, log

def calculadora (valor, funcion):
    for i in range (1, valor + 1):
        if funcion > 3 :
            if funcion > 4 :
                resultado = log(i)
            else :
                resultado = exp(i)
        elif funcion < 2 :
            resultado = sin(i)
        elif funcion == 3 :
            resultado = tan(i)
        else :
            resultado = cos(i)
        print(f'{i}\t{resultado}')

operacion = int(input('1-Seno\n2-Coseno\n3-Tangente\n4-Exponencial\n5-Logaritmo Neperiano\nIngrese operación a realizar: '))
num = int(input('Ingrese valor: '))

calculadora(num, operacion)



# OTRAS SOLUCIONES

# 1

from math import sin, cos, tan, exp, log

def apply_function(f, n):
    functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    result = {}
    for i in range(1, n+1):
        result[i] = functions[f](i)
    return result

def calculator():
    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    for i, j in apply_function(f, n).items():
        print (i, '\t', j)
    return

calculator()

# 2

from math import sin, cos, tan, exp, log

def apply_function(f, n):
    result = {}
    for i in range(1, n+1):
        result[i] = eval(f + '(' + str(i) + ')')
    return result

def calculator():
    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    for i, j in apply_function(f, n).items():
        print (i, '\t', j)
    return

calculator()


# 3

from math import sin, cos, tan, exp, log

def calculator():
    functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    results = [functions[f](x) for x in range(1, n+1)]
    for i in range(n):
        print (i + 1, '\t', results[i])
    return

calculator()