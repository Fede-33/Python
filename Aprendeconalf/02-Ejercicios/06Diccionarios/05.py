# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

curso = {
    'Matemáticas': 6, 
    'Física': 4, 
    'Química': 5
}
total = 0

for i in curso:
    print(f'{i} tiene {curso[i]} créditos.')
    total += curso[i]

print(f'El total de créditos es de: {total}')


#Otra forma:
total = 0

for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    total += creditos
print(f'Número total de créditos del curso: {total}')