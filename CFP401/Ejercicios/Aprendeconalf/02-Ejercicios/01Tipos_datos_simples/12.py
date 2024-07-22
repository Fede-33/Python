# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

pan = int(input('Cantidad de pan viejo vendido: '))

subt = pan * 3.49
total = round(subt*0.6, 2)

print(f'El precio habitual del pan es de \N{euro sign}3.49, la cantidad vendida es de {subt}, con descuento aplicado es \N{euro sign}{total}' )