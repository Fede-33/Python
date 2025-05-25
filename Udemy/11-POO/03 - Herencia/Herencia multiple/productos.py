class Pc:
    def __init__(self):
        print('PC')
    def ram(self):
        print('32 GB')
    def cpu(self):
        print('Ryzen 9')

class Laptop:
    def __init__(self):
        print('Laptop')

class Monitor:
    def __init__(self):
        print ('Monitor')
    def pant(self):
        print ('Monitor Externo')
    def touch(self):
        print ('No touchscreen')
    def resol (self):
        print('4K')

class Pantalla:
    def pant(self):
        print ('Pantalla Integrada')
    def touch(self):
        print ('Touchscreen')
    def resol (self):
        print('Ful HD')

class Perif:
    def mouse (self):
        print('Mouse incluído')
    def teclado (self):
        print('teclado incluído')
    def parlantes (self):
        print('parlantes incluídos')        

class Msi (Laptop, Pc, Pantalla, Perif):
    def resol(self):
        print('4K')

class Pc_Gamer (Pc, Monitor, Perif):
    def parlantes (self):
        print('parlantes no incluídos')

