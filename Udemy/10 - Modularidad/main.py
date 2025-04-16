import Paquetes.aritmetica as artm

def main():
    suma = artm.sumar(4,4,5,8,7,9)
    resta = artm.restar(10,5)
    potencia = artm.potenciar(3, 3)

    print(f'Suma: {suma}\nResta: {resta}\nPotencia: {potencia}')

if __name__ == '__main__': 
    main()