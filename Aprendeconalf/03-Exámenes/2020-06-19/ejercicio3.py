# Escribir un programa para gestionar las citas de una consulta médica. La base de datos de citas debe estar en un fichero de nombre citas.csv. Cada cita contendrá los campos dni, mes, dia, hora y especialidad. No es necesario que la primera fila del csv contenga los nombres de los campos. El programa debe incluir las siguientes funciones:

from datetime import datetime

    #1 Una función que permita generar el fichero y añadir una cita a la base de datos.

path = './3_files/citas.csv'

def crear(ruta):
    registro = []
    campos = ['DNI', 'mes', 'día', 'hora', 'especialidad']

    try:
        f = open (ruta, 'a')
    except FileNotFoundError:
        f = open(ruta, 'w')
    
    for i in campos:
        registro.append(input(f'Ingrese {i}: '))
    
    registro = str(registro).replace('[','').replace(']','').replace("'","")
    f.write(f'{registro}\n')
    f.close()
    print('Cita agendada con éxito')


    #2 Una función que reciba un dni y devuelva una lista con las citas de ese paciente.

def listar(ruta) :
    f = open(ruta, 'r')
    citas = f.readlines()
    registro = []

    dni = input('Ingrese DNI a consultar: ')

    for i in citas:
        if i.split(',')[0] == dni:
            registro.append(i.replace('\n','').split(','))

    f.close()
    return registro, dni

    #3 Una función para eliminar las citas anteriores a una fecha dada.

def eliminar(ruta):
    ingreso = input('Ingrese la fecha (DD/MM/AAAA): ')
    fecha = datetime.strptime(ingreso, '%d/%m/%Y')

    f = open(ruta, 'r')
    registros = f.readlines()
    f.close()
    f = open(ruta,'w')
    
    for i in registros:
        fechacita = f'{i.split(",")[2]}/{i.split(",")[1]}/{datetime.now().year}'
        fechacita = datetime.strptime(fechacita, ' %d/ %m/%Y')

        if fecha <= fechacita:
            f.write(i)
    
    f.close()    
        
#MENU

op = 1
while op != 4: 
    try:
        op = int(input('''       
            MENU
      
    1 - Agregar cita.
    2 - Consulta por DNI.
    3 - Eliminar historial.
    4 - Salir.
      
    Ingrese su opción: '''))
        
        if op == 1:
            crear(path)
        elif op == 2:
            lista, dni = listar(path)
            if lista:
                print(f'\nLas citas del cliente DNI {dni} son:\n')
                for i in lista:
                    print (f'Mes: {i[1]} Día: {i[2]} Hora: {i[3]} Especialidad: {i[4]}' )
            else:
                print(f'El cliente DNI {dni} no tiene citas')
        elif op == 3:
            eliminar(path)
        elif op == 4:
            print('\n   Adios.')
        else:
            print('\n   Opción incorrecta, inténtelo otra vez')


    except ValueError:
        print('\n   Opción incorrecta, inténtelo otra vez')

