# Realizar un programa que pregunte al usuario por un número entero impar y dibuje un rombo con el número de filas introducidas por el usuario.

while True:
    try:
        nro = int(input('Ingrese un número entero impar: '))
        if nro % 2 == 0 or nro < 1:
            raise ValueError
        else:
            break
    except ValueError:
        print('\nError, inténtelo otra vez\n')

var = (nro//2)

for i in range(1, var+1):
    print((' ' * (var-i)) , ( '*' * (2*i - 1)))

print('*'*nro)

for i in range (var, 0, -1):
    print((' ' * (var-i)) , ('*' * (2*i - 1)))     

