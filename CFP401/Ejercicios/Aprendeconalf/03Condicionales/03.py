# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

num = float(input('Ingrese numerador: '))
den = float(input('Ingrese denominador: '))

if den == 0 :
    print('\nNo se puede dividir por 0')
else :
    print('\nResultado:', num / den)