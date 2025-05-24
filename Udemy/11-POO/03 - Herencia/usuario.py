class Usuario:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def detalle_usuario(self):
        print(f'Nombre: {self.nombre}\nEdad: {self.edad}')
    
class Cliente(Usuario):
    pass

class Empleado(Usuario):
    
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def detalle_empleado(self):
        Usuario.detalle_usuario(self)
        print(f'Sueldo: {self.sueldo}')