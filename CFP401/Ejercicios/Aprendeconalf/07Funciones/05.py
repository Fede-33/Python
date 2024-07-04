# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

def area (rad):
    return 3.14 * (rad**2)

def volum(area, alt):
    return area * alt

radio = float(input('Ingrese radio del círculo: '))
altura = float(input('Ingrese altura del cilindro: '))

print (f'Su área es {area(radio)} y su volumen es {volum(area(radio), altura)}')