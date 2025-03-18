# Escribir un programa que calcule a partir de una fecha de un año no bisiesto el número de días que han transcurrido en ese año y el número de meses lunares completos que abarcan. Se recuerda que un mes lunar dura aproximadamente 29,53 días. El programa debe usar diccionarios para acceder al número de días de cada mes.

calendario = {"enero":31, "febrero":28, "marzo":31, "abril":30, "mayo":31, "junio":30, "julio":31, "agosto":31, "septiembre":30, "octubre":31, "noviembre":30, "diciembre":31}

print("CALENDARIO LUNAR")
print("Este programa convierte una fecha de un año NO bisiesto a un calendario lunar.")

while True:
    try:
        dia = int(input('Ingrese día: '))
        mes = input('Ingrese mes: ').lower()
        if mes not in calendario.keys():
            print(f'El mes de {mes} no existe.')
            raise ValueError
        if dia < 1 or dia > calendario[mes]:
            print(f'El día {dia} del mes de {mes} no existe.')
            raise ValueError
        
        contador = 0
        for i in calendario.keys():
            if i != mes:
                contador += calendario[i]
            else:
                contador += dia
                break

        print(f'El día {dia} de {mes} es el día nro. {contador} del año')
        print(f'Habrán pasado {round((contador / 29.53), 2)} meses lunares')
        break

    except ValueError:
        print('Intentelo otra vez.\n')

