from figuras import Rectangulo, Circulo, probar_figura

def main():
    while True:
        try:
            print('1-Rectángulo / 2-Círculo / 3-Salir')
            opc = int(input('Ingrese opción: '))
            if opc < 0 or opc > 3:
                raise ValueError
            elif opc == 1:
                base = float(input('Ingrese valor de la base: '))
                altura = float(input('Ingrese valor de la altura: '))
                fig = Rectangulo('Rectángulo', base, altura)
            elif opc == 2:
                radio = float(input('Ingrese valor del radio: '))
                fig = Circulo('Círculo', radio)
            else:
                break
            probar_figura(fig)    
        except ValueError:
            print ('Ingreso incorrecto.\n')
        
if __name__ == '__main__':
    main()