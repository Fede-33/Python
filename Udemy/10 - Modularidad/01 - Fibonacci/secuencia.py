# Crear un modulo que genere una secuencia de Fibonacci, dentro de este módulo crea dos funciones:
# La primera función que genere la secuencia de Fibonacci con números

def fibo (n):
    a , b = 0 , 1
    for _ in range(n):
        print(a, end=', ')
        a , b = b , (a + b)

# La segunda función que retorne una lista de secuencia de Fibonacci
def lista_fibo(n):
    res = []
    a , b = 0 , 1
    for _ in range(n):
        res.append(a)
        a , b = b , (a + b)
    return res
