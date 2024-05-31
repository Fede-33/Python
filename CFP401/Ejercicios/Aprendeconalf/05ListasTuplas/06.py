# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
notas = []

for i in range(len(asignaturas)):
    notas.append(float(input(f'Ingrese su calificación en {asignaturas[i]}: ')))
    
for i in range(len(notas)):    
    if notas[i] >= 7:
        asignaturas.pop(i)

print(f'Debe recursar {asignaturas}.')