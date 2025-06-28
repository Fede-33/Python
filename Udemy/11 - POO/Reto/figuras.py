import math

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'{self.nombre}' 

class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perim(self):
        return (self.base + self.altura)*2
    
    def __str__(self):
        return super().__str__() + f' de base: {self.base} y altura: {self.altura}'
    
class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def area(self):
        return math.pi * (self.radio)**2
    
    def perim(self):
        return math.pi * self.radio * 2
    
    def __str__(self):
        return super().__str__() + f' de radio: {self.radio} y diámetro: {self.radio * 2}'

def probar_figura(obj):
    print('\n' + f'{obj}')
    print(f'Área: {round(obj.area(),2)}')
    print(f'Perímetro: {round(obj.perim(),2)}\n')

    