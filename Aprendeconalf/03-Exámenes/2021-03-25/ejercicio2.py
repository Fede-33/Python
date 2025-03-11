# Juan juega siempre la misma combinación a la bonoloto: 7, 13, 21, 37, 46, 49.

#Construir un programa que pregunte al usuario por la combinación ganadora y diga si Juan ha ganado o, en caso contrario, muestre por pantalla la lista de los números que no ha acertado. El programa debe usar listas.

#Nota: El juego de la bonoloto consiste en acertar una combinación de 6 números entre 1 y 49.

juan = [7, 13, 21, 37, 46, 49]
gana = [7, 13, 21, 37, 47, 49]


for i in juan:
    if i in gana:
        gana.remove(i)
    
if not gana:
    print('Juan ha ganado.')
else:
    print(f'Juan falló los números: {gana}')