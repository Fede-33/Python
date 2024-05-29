# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

def ingreso(dato):
    flag = True
    while flag:
        try:
            valor = float(input(f'Ingrese {dato}'))
            flag = False
        except ValueError:
            print('Ingreso incorrecto.\n')
    return valor

dict = {
    'cantidad a invertir: $': None,
    'Interés anual: %': None, 
    'cantidad de años: ': None
    }

for i in dict:
    dict[i] = ingreso(i)

for i in range(1, int(dict['cantidad de años: ']+1)):
    dict['cantidad a invertir: $'] *= (1 + dict['Interés anual: %'] / 100)
    print(f'El capital tras {i} años es de ${round(dict['cantidad a invertir: $'], 2)}')