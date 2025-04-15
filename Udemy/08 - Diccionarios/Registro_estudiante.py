registro = []
estudiante = {'nombre':'', 'edad':'', 'curso':''}

while True:
    continuar = input('¿Agregar nuevo estudiante? (S/N) ').upper()
    if continuar == 'N':
        break
    estudiante = {'nombre':'', 'edad':'', 'curso':''}
    for i in estudiante:
        estudiante[f'{i}'] = input(f'Ingrese {i}: ')
    registro.append(estudiante)

print('REGISTRO DE ESTUDIANTES')
for i in registro:
    print(f'Nombre: {i['nombre']} | Edad: {i['edad']} | Curso: {i['curso']}')
        
