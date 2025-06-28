class Usuario:

    def __init__(self, nombre, contras, palabra):
        self.nombre = nombre
        self.__contras = contras
        self.__palabraclave = palabra

    def __ver_contras(self, palabra):
        if self.__palabraclave == palabra:
            print(f'Contraseña: {self.__contras}')
        else:
            print('Palabra clave incorrecta.')

    def __cambiar_contras(self, contras):
        if self.__contras == contras:
            nuevacont = str(input('Ingrese nueva contraseña: '))
            self.__contras = nuevacont
            print('Contraseña cambiada.')
        else:
            print('Contraseña incorrecta.')

    def __str__(self, contras):
        if self.__contras == contras:
            return f'Nombre: {self.nombre}\nContraseña: {self.__contras}\nPalabra Clave: {self.__palabraclave}'
        else:
            print('Contraseña incorrecta.')

    def menu(self):
        while True:
            print('''---MENU---
                  1 - Ver contraseña.
                  2 - Cambiar contraseña.
                  3 - Ver todos los datos.
                  4 - Salir.''')
            try:
                opc = int(input('Ingrese Opción: '))
                if opc < 1 or opc > 4:
                    raise ValueError
                elif opc == 1:
                    palabra = str(input('Ingrese palabra clave: '))
                    self.__ver_contras(palabra)
                elif opc == 2:
                    contras = str(input('Ingrese contraseña: '))
                    self.__cambiar_contras(contras)
                elif opc == 3:
                    contras = str(input('Ingrese contraseña: '))
                    print(self.__str__(contras))
                else:
                    print('Adios.')
                    break
            except ValueError:
                print('Opción incorrecta:')
    
