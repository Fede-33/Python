# 2 Diseñe un programa que le pida al usuario cinco (5) números y los agregue uno a uno a una lista. Puede utilizar funciones de python como append().

lista=[]

for i in range(5):
    valor = None
    while not valor:
        try:
            valor = float(input('Ingrese un número: '))
            lista.append(valor)
        except ValueError:
            print('Valor incorrecto\n')

# 3 Utilizando la lista de números creada en el ejercicio anterior determine la suma total de la lista, es decir sume todos los números de la misma. No puede utilizar la función sum() de listas de python.
suma = 0

for i in lista:
    suma += i

print(f'La suma total de los nùmeros es {suma}')

# 4 Sobre la misma lista de números ahora calcule el promedio, para esto necesita determinar el número total de elementos de la lista, use la función len(lista_numericas)

promedio = suma / len(lista)

print(f'El promedio de los valore es {promedio}')