# Detectar y corregir los errores del siguiente programa que aplica el iva a una factura:
'''
base = input('Introduce la base imponible de la factura: ')
print(aplica_iva(base, iva))

def aplica_iva(base, iva = 21):
    base = base * iva   
    return base 
'''

def aplica_iva(base, iva = 21):
    base += base * iva / 100   
    return base 

base = float(input('Introduce la base imponible de la factura: '))
print(aplica_iva(base))


