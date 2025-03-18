# Un n-grama es una secuencia de N caracteres consecutivos de una cadena. Por ejemplo, los 3-gramas de la cadena 'Python' son 'Pyt', 'yth', 'tho' y 'hon'. Escribir un programa que pregunte por una cadena y un número entero positivo y muestre por pantalla todos los n-gramas de la cadena.

cadena = input('Ingrese una palabra: ')
entero = int(input('Ingrese un número entero: '))

for i in (range(len(cadena) - entero + 1)):
    print(cadena[i:i+entero])