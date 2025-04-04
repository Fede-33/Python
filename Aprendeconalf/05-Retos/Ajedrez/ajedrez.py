import keyboard as kb
import threading as thrd
import os

# Tarea 1: La primera tarea consiste en escribir un programa que guarde en un fichero la secuencia de tableros de una partida de ajedrez. Partiremos del tablero inicial donde las filas del tablero están separadas por cambios de línea y las columnas por tabuladores. El programa debe guardar el tablero inicial en un fichero con el nombre que elija el usuario.  

tablero = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖\n'
nombre = input('ingrese nombre de partida: ')

with open(f'./{nombre}.txt', 'w', encoding='utf-8') as f:
    f.write(tablero)

#Después debe preguntar al usuario si quiere hacer un movimiento o terminar la partida. Cada vez que el usuario quiera hacer un nuevo movimiento debe preguntar la fila y la columna de la pieza que quiere mover y la fila y la columna a la que la quiere mover. Tras ello añadirá el tablero resultante al final del fichero anterior.

terminar = False

def final() :
    global terminar
    while True:
        if kb.is_pressed('esc'):
            print('\n\nFin del programa.')
            terminar = True
            os._exit(0)
            break

def ingreso():
    global coor_pieza, coor_dest, lineas
    try:
        print('\t\tPRESIONE ESC PARA FINALIZAR.')
        with open(f'./{nombre}.txt', 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            for i in range(len(lineas)-8, len(lineas)):
                lineas[i] = lineas[i].replace('\n', '').split('\t') 
                print('\t'.join(lineas[i]))
        pieza_x = int(input('ingrese coordenada X de la pieza: '))
        pieza_y = int(input('ingrese coordenada Y de la pieza: '))
        dest_x = int(input('ingrese coordenada X destino: '))
        dest_y = int(input('ingrese coordenada Y destino: '))
        for i in [pieza_x, pieza_y, dest_x, dest_y]:
            if i not in range(1,9):
                raise ValueError
    except ValueError:
        if terminar == False:
            print ('Coordenada incorrecta. \n')
    else:
        coor_pieza = [(pieza_x - 1), (pieza_y - 1)]
        coor_dest = [(dest_x - 1), (dest_y - 1)]

hilo_fin = thrd.Thread(target = final)
hilo_fin.daemon = True
hilo_fin.start()

while True: 
    hilo_input = thrd.Thread(target=ingreso)
    hilo_input.daemon = True
    hilo_input.start()
    hilo_input.join()
    if terminar:
        terminar = False
        break
    pieza = lineas[7-(coor_pieza[1])][coor_pieza[0]]
    lineas[7-(coor_pieza[1])][coor_pieza[0]] = ''
    lineas[7-(coor_dest[1])][coor_dest[0]] = pieza
    with open(f'./{nombre}.txt', 'a', encoding='utf-8') as f:
        for fila in lineas:
            f.write('\t'.join(fila) + '\n')




    




# Tarea 2: Una vez generado el fichero con los tableros sucesivos de una partida de ajedrez, el programa preguntará por un movimiento y mostrará por pantalla el tablero correspondiente ese movimiento. Por ejemplo, utilizando el fichero partida-ajedrez.txt, si el usuario introduce el movimiento 2, debería mostrar por pantalla el siguiente tablero: