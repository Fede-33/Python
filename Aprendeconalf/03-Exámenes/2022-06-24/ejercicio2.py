# Realizar un programa que simule el juego de las tres en raya. Cada jugador solo debe colocar su ficha una vez por turno y no debe ser sobre una casilla ya ocupada. En caso de que el jugador haga trampa el ganador será el otro. Para ganar se debe conseguir realizar una línea recta (horizontal, vertical o diagonal) con la misma ficha. El tablero es de 3x3 y cualquier casilla podrá estar vacía u ocupada sólo por una ficha X o 0. El programa debe realizar las siguientes operaciones:

    # Mostrar el tablero por pantalla.
    # Poner una ficha en una cuadricula comprobando que no está ocupada.
    # Comprobar si se produce tres en raya e indicar si es de X o de O, o si hay empate.

tablero = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
signos = ['O', 'X']

def imprimir(tablero):
    print('\n')
    for linea in tablero:
        print (f'\t\t{linea}')

imprimir(tablero)

for intentos in range(9):
    print(f'TURNO: {signos[intentos%2]}')
    ganador = False

    while True:
        try:
            x = int(input('\nIntroduce coordenada X: '))
            y = int(input('Introduce coordenada Y: '))

            if tablero[y-1][x-1] == ' ':
                tablero[y-1][x-1] = signos[intentos%2]
            else: 
                print('Espacio ocupado, inténtelo otra vez\n')
            imprimir(tablero)
            break
        
        except :
            print('Coordenadas incorrectas, inténtelo otra vez\n')
            imprimir(tablero)

    for indice in range(3):
        if tablero[indice][0] == tablero[indice][1] == tablero[indice][2] != ' ' or tablero[0][indice] == tablero[1][indice] == tablero[2][indice] != ' ' or tablero[1][1] == tablero[2][2] == tablero[0][0] != ' ' or tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
            ganador = True

    if ganador == True:
        print(f'\n\t\tGANADOR: {signos[intentos%2]}\n')
        break 

if ganador == False:
    print('\n\t\tEMPATE\n')
        
    
    


    
