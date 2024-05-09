# Calcule la llegada de un transporte cuyo itinerario determinado es de 10 horas, sin embargo, permita ingresar otra cantidad de tiempo

from datetime import timedelta, datetime

def arribo(horas=10):
    horario = datetime.now() + timedelta(hours=horas)
    print (horario.strftime("Llega el %A a las %H:%M"))

tiemp = input("Ingrese tiempo de viaje: ") or False

arribo(tiemp)

#PREGUNTAR!!!
#TRY CATCH
            