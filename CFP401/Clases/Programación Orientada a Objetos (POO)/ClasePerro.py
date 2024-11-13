class Perro:
    def __init__(self, nombre, raza, edad):
        # tiene tres atributos: nombre, raza y edad
        self.nombre = nombre    #publicos  
        self.raza = raza        #publicos
        self.edad = edad        #publicos

    # tiene un metodo o una responsabilidad: ladrar
    def ladrar(self):
        print(self.nombre + " está ladrando: ¡Guau, guau!")

# En este punto finalizo la definicion de mi CLASE
# Crear una instancia de la clase Perro
boby = Perro("Boby", "Del Barrio", 3)

molly = Perro("Molly", "Caniche", 7)
wanda = Perro("Wanda", "Caniche", 2)
thor = Perro("Thor", "Raza de Odin", 200)

# Llamar al método ladrar
boby.ladrar()
thor.ladrar()
wanda.ladrar()
#acceso a los atributos publicos

print("La raza de boby es: " + boby.raza)
