# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input('Ingrese edad: '))
ing = float(input('Ingrese ingresos mensuales: '))

if edad > 16 :
    if ing > 1000 :
        print('\nDebe tributar.')
    else:
        print('\nPagale bien, miserable.')
else :
    print ('\nLargá al pibe, pedazo de esclavista.')