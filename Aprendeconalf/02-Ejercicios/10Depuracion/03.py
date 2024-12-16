# Detectar y corregir los errores del siguiente programa que calcula el producto escalar de dos vectores:

'''
u = (1, 2, 3)
v = (4, 5, 6)

def producto_escalar(u, v):
    for i in u:
        u[i+1] *= v[i+1]
    return sum(u)

print(producto_escalar(u, v))
'''

u = [1, 2, 3]
v = [4, 5, 6]

def producto_escalar(u, v):
    for i in range(len(u)):
        u[i] *= v[i]
    return sum(u)

print(producto_escalar(u, v))