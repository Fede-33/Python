class Persona:
    nombre = None
    edad = None

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')


class PersonaCons:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')

    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}'