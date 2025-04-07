#1 La primera tarea consiste en construir un laberinto como el de la siguiente figura. El laberinto se representará como una una lista de listas, donde cada lista es una fila del laberinto y cada casilla se representará con un espacio ' ' si hay paso o con la letra 'X' si hay un muro

def construir(dimension, muros):
    laberinto = []
    for i in range(dimension):
        fila = []
        for j in range(dimension):
            if tuple([i, j]) in muros:
                fila.append('X')
            else:
                fila.append(' ')
        laberinto.append(fila)
    return laberinto

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
laberinto = construir(5, muro)   

for i in laberinto:
    print(''.join(i))

#2 construir un programa para recorrer el laberinto desde la entrada a la salida. La entrada siempre está en la esquina superior izquierda y la salida en la esquina inferior derecha. El programa debe devolver una lista con la secuencia de movimientos para ir de la entrada a la salida del laberinto.

def recorrer(laberinto, dimension):
    fila, columna = 0, 0
    camino = [(0, 0)]
    visitados = set([(0, 0)])
    movimientos = []

    def es_valido(f, c):
        return 0 <= f < dimension and 0 <= c < dimension and laberinto[f][c] == ' ' and (f, c) not in visitados

    def buscar_camino():
        nonlocal fila, columna
        if fila == dimension - 1 and columna == dimension - 1:
            return True

        # Intentar ir Abajo
        nueva_fila, nueva_columna = fila + 1, columna
        if es_valido(nueva_fila, nueva_columna):
            fila, columna = nueva_fila, nueva_columna
            camino.append((fila, columna))
            visitados.add((fila, columna))
            movimientos.append('Abajo')
            if buscar_camino():
                return True
            movimientos.pop() # Backtrack
            camino.pop()
            fila, columna = camino[-1]

        # Intentar ir Derecha
        nueva_fila, nueva_columna = fila, columna + 1
        if es_valido(nueva_fila, nueva_columna):
            fila, columna = nueva_fila, nueva_columna
            camino.append((fila, columna))
            visitados.add((fila, columna))
            movimientos.append('Derecha')
            if buscar_camino():
                return True
            movimientos.pop() # Backtrack
            camino.pop()
            fila, columna = camino[-1]

        # Intentar ir Arriba
        nueva_fila, nueva_columna = fila - 1, columna
        if es_valido(nueva_fila, nueva_columna) and (nueva_fila, nueva_columna) not in camino: # Evitar retroceso inmediato
            fila, columna = nueva_fila, nueva_columna
            camino.append((fila, columna))
            visitados.add((fila, columna))
            movimientos.append('Arriba')
            if buscar_camino():
                return True
            movimientos.pop() # Backtrack
            camino.pop()
            fila, columna = camino[-1]

        # Intentar ir Izquierda
        nueva_fila, nueva_columna = fila, columna - 1
        if es_valido(nueva_fila, nueva_columna) and (nueva_fila, nueva_columna) not in camino: # Evitar retroceso inmediato
            fila, columna = nueva_fila, nueva_columna
            camino.append((fila, columna))
            visitados.add((fila, columna))
            movimientos.append('Izquierda')
            if buscar_camino():
                return True
            movimientos.pop() # Backtrack
            camino.pop()
            fila, columna = camino[-1]

        return False

    if buscar_camino():
        return movimientos
    else:
        return ['No se encontró salida']

print('Solución: ', recorrer(laberinto, 5))