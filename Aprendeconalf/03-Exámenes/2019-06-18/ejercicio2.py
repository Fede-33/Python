# A lo largo de un curso se realizan dos exámenes parciales. Para aprobar el curso la nota media debe ser mayor o igual que 5 siempre y cuando en ambos parciales se tenga al menos un 4. Escribir un programa que pregunte al usuario la nota de los dos parciales y muestre por pantalla si el alumno ha aprobado el curso o si no, y en caso de no haber aprobado, qué parcial tiene que repetir por tener menos de 4 en él.

nota_1 = float(input('Ingrese nota del primer parcial: '))
nota_2 = float(input('Ingrese nota del segundo parcial: '))

if nota_1 >= 4:
    if nota_2 >= 4:
        media = (nota_1 + nota_2)/2
        if media >= 5:
            print("Curso aprobado")
        else:
            print("Curso desaprobado, no llega a 5 en la media")
    else:
        print("Debe repetir el segundo parcial")
else:
    print("Debe repetir el primer parcial")
    if not nota_2 >= 4:
        print("Debe repetir el segundo parcial")
    
