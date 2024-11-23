# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0 (Inaceptable), 0.4(Aceptable), 0.6 o más(Meritorio), pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel. Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

punt = None

def rta(nivel, pago) :
    print (f'Rendimiento {nivel} recibe aumento de €{pago * 2400}' )

while punt == None :
    try:
        punt = float(input('Ingrese puntuación: '))
        if punt != 0.0 and punt != 0.4 and punt <= 0.6 :
            punt = None
            raise RuntimeError 
    except (ValueError, RuntimeError) :
        print('Valor incorrecto.\n')

if punt == 0.0 :
    rta('Inaceptable', punt)
elif punt == 0.4 :
    rta('Aceptable', punt)
else :
    rta('Meritorio', punt)