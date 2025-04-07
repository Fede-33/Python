import keyboard as kb
import threading as thrd
import sys
import os

# Tarea 1: La primera tarea consiste en escribir un programa que guarde en un fichero la secuencia de tableros de una partida de ajedrez. Partiremos del tablero inicial donde las filas del tablero están separadas por cambios de línea y las columnas por tabuladores. El programa debe guardar el tablero inicial en un fichero con el nombre que elija el usuario.  

tablero = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖\n'
nombre = input('ingrese nombre de partida: ')

with open(f'./{nombre}.txt', 'w', encoding='utf-8') as f:
    f.write(tablero)

#Después debe preguntar al usuario si quiere hacer un movimiento o terminar la partida. Cada vez que el usuario quiera hacer un nuevo movimiento debe preguntar la fila y la columna de la pieza que quiere mover y la fila y la columna a la que la quiere mover. Tras ello añadirá el tablero resultante al final del fichero anterior.


def finjuego():
    global terminar
    terminar = False
    while True:
        if kb.is_pressed('esc'):
            terminar = True
            print('\n\nFin del Juego. Presione cualquier tecla para continuar.')
            break

def final():
    global terminar
    terminar = False
    while True:
        if kb.is_pressed('esc'):
            terminar = True
            print('\n\nFin del programa.')
            os.system('pause')
            sys.exit(0)
            break

def ingreso():
    coordenadas = {'X de la pieza':'', 'Y de la pieza':'', 'X destino':'', 'Y destino':''}
    try:
        print('\t\tPRESIONE ESC PARA FINALIZAR.')
        with open(f'./{nombre}.txt', 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            lineas = [fila.replace('\n', '').split('\t') for fila in lineas[-8:]]
            for fila in lineas:
                print('\t'.join(fila))
        for i in coordenadas.keys():
            if terminar:
                return None, None, None
            coordenadas[i] = int(input(f'ingrese coordenada {i}: '))
            if coordenadas[i] not in range(1, 9):
                raise ValueError
    except ValueError:
        if not terminar:
            print('Coordenada incorrecta. \n')
        return None, None, None
    coor_pieza = [(coordenadas['X de la pieza'] - 1), (coordenadas['Y de la pieza'] - 1)]
    coor_dest = [(coordenadas['X destino'] - 1), (coordenadas['Y destino'] - 1)]
    return coor_pieza, coor_dest, lineas

hilo_fin = thrd.Thread(target=finjuego)
hilo_fin.daemon = True
hilo_fin.start()

while not terminar:
    coor_pieza, coor_dest, lineas = ingreso()
    if terminar:  
        break
    elif coor_pieza is not None:
        pieza = lineas[7 - coor_pieza[1]][coor_pieza[0]]
        lineas[7 - coor_pieza[1]][coor_pieza[0]] = ''
        lineas[7 - coor_dest[1]][coor_dest[0]] = pieza
        with open(f'./{nombre}.txt', 'a', encoding='utf-8') as f:
            for fila in lineas:
                f.write('\t'.join(fila) + '\n')

hilo_fin = thrd.Thread(target=final)
hilo_fin.daemon = True
hilo_fin.start()

while not terminar:
    print('\n\t\tPRESIONE ESC PARA FINALIZAR.')
    try:
        mov = int(input('Ingrese el movimiento a consultar: '))
        with open(f'./{nombre}.txt', 'r', encoding='utf-8') as f:
            consulta = f.readlines()
        for i in range(mov*8, (mov*8)+8):
            print (consulta[i].replace('\n', ''))
    except (ValueError, IndexError):
        if not terminar:
            print('Movimiento inexistente.\n')
    


# Tarea 2: Una vez generado el fichero con los tableros sucesivos de una partida de ajedrez, el programa preguntará por un movimiento y mostrará por pantalla el tablero correspondiente ese movimiento: