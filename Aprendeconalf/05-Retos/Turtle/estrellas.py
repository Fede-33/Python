from turtle import *

def dibujar(n):
    speed(5)  
    for i in range(n):
        forward(100)
        right(180 - (180 / n))
    mainloop()

while True:
    try:
        puntas = int(input('Ingrese cantidad de puntas de la estrella: '))
        if puntas < 3:
            raise ValueError
        dibujar(puntas)
        break
    except ValueError:
        print('\nValor Incorrecto\n')
    



