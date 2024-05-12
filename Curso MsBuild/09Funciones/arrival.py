# Calcule la llegada de un transporte cuyo itinerario determinado es de 10 horas, sin embargo, permita ingresar otra cantidad de tiempo

from datetime import timedelta, datetime

tiemp = -1
def arribo(horas=10):
    horario = datetime.now() + timedelta(hours=horas)
    print (horario.strftime("Llega el %A a las %H:%M"))

while tiemp < 0:
    try:
        tiemp = int(input("Ingrese cantidad de horas de viaje: "))
        if tiemp < 0:
            raise RuntimeError
    except (ValueError, RuntimeError):
        print ('Ingrese un número entero de horas \n')

if tiemp:
    arribo(tiemp)
else:
    arribo()


            