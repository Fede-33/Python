# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = int(input('Ingrese cantidad de horas: '))
coste = int(input('Costo por hora: '))

print('Le corresponde:', horas*coste)