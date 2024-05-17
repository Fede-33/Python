

def maximo(num1, num2):
    if num1 < num2 :
        return f"El máximo es {num2}"
    elif num1 == num2 :
        return f"Los números {num1} y {num2} son iguales."
    else:
        return f"El máximo es {num1}" 

def ing():
    return float(input('Ingrese número real: '))

n1 = ing()
n2 = ing()

print(maximo(n1, n2))