asignaturas = ('Matemáticas', 'Física', 'Química', 'Historia', 'Lengua')
recursa = []

for i in asignaturas:
    nota = float(input(f'Ingrese su calificación en {i}: '))
    if nota < 7:
        recursa.append(i)

print(f'Debe recursar {recursa}.')