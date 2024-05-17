# Realiza  una  función  que  dado  dos  números  retorne  el  mínimo  de  ambos.  La  función debe llamarse, por ejemplo, así: minimo(num1, num2). Ejemplo si ingreso minimo(10, 8) debe retornar el 8.

def minimo(num1, num2):
    if num1 > num2 :
        return f"El mínimo es {num2}"
    elif num1 == num2 :
        return f"Los números {num1} y {num2} son iguales."
    else:
        return f"El mínimo es {num1}" 

def ing():
    return float(input('Ingrese número real: '))

n1 = ing()
n2 = ing()

print(minimo(n1, n2))