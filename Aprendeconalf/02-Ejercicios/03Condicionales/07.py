# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# <€10000 5%
# <€20000 15%
# <€35000 20%
# <€60000 30%
# >€60000 45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

renta = None

def rta(n) :
    print(f'El tipo impositivo es {n}%')

while renta == None :
    try: 
        renta = float(input('Ingrese renta anual €'))
    except ValueError:
        print('\nValor incorrecto.\n')

if renta > 60000 :
    rta(45) 
elif renta > 35000 :
    rta(30) 
elif renta > 20000 :
    rta(20) 
elif renta > 10000 :
    rta(15) 
elif renta > 10000 :
    rta(5)
else :
    print ('No tributa.')
    
