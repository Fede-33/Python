# Crear una función para determinar el área de un cuadrado. La misma debe solicitar el lado  del  cuadrado.  Tenga  en  cuenta  que  el  área  de  un  cuadrado  se  calcula  de  la siguiente manera: uno de sus lados elevado al cuadrado (Área = a2), es decir: El área del cuadrado de lado 5 cm es de 25 cm2.

def areacuad(lado):
    return lado ** 2

num = float(input('Ingrese el lado del cuadrado: '))

print(f'El área de un cuadroado de {num}cm de lado, es igual a {areacuad(num)}cm.')