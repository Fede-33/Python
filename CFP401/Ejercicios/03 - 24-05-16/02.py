# Realiza  una  función  llamada  area_rectangulo(base,  altura)  que  devuelva  el  área  del rectángulo a partir de una base y una altura. Recordar que el área de un rectángulo se obtiene al multiplicar la base por la altura.

def area_rectangulo(b, h):
    return b * h

base = float(input('Ingrese valor de la base: '))
altura = float(input('Ingrese valor de la altura: '))

print(f'El área del rectángulo es de {area_rectangulo(base, altura)}')