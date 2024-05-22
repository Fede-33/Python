# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
edad = None

def rta(n) :
    print(f'Debe abonar {n}€')
    
while edad == None:
    try :
        edad = int(input('Ingrese edad: '))
    except ValueError :
        print ('Valor incorrecto.\n')

if edad > 18 :
    rta(10)
elif edad > 4:
    rta(5)
else: 
    print('Entrada gratuita.')