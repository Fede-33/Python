# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

inv = float(input('Cantidad a invertir: '))
inter = float(input('Interés anual: '))
tiemp = int(input('Cantidad de años: '))

cap = inv * (inter/100 + 1)**tiemp

print('El capital final será:', round(cap, 2))