# Un cine tiene una sala rectangular con 5 filas y 4 columnas de butacas. Escribir un programa que permita gestionar la reserva de butacas con los siguientes requisitos:

matriz = ['XXXXX','XXXXX','XXXXX','XXXXX']
resp = 's'

while resp == 's':

    try:
        print('RESERVA DE BUTACAS')
        for i in matriz:
            print(i)

        fila = int(input('\nIntroduce la fila: '))
        colu = int(input('Introduce la columna: '))

        linea = list(matriz[fila-1])
        if linea[colu-1] == 'O':
            print('La butaca está ocupada.\n')
        else: 
            linea[colu-1] = 'O'
            print('Reserva realizada.\n')
            matriz[fila-1] = ''.join(linea)
    
    except IndexError or ValueError:
        print('Las filas o columnas son incorrectas.\n')

    while True:    
        try:
            resp = input('¿Continuar reservando? (S/N): ').lower()
            if resp == 's' or resp == 'n':
                break 
            else:
                raise ValueError
        except:
            print('Respuesta incorrecta.\n')
