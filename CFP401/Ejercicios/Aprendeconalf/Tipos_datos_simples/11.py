# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.


inv = float(input('Cantidad a invertir: '))

cap1 = inv * (0.47 + 1)
cap2 = inv * (0.47 + 1)**2
cap3 = inv * (0.47 + 1)**3
print('El capital final al primer año:', round(cap1, 2))
print('El capital final al segundo año:', round(cap2, 2))
print('El capital final al segundo año:', round(cap3, 2))