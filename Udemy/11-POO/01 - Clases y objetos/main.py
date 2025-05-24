from persona import Persona, PersonaCons

persona1 = Persona()
persona1.nombre = 'Alex'
persona1.edad = 25

persona2 = Persona()
persona2.nombre = 'Ana'
persona2.edad = 22

persona1.mostrar_datos()
persona2.mostrar_datos()

persona3 = PersonaCons('Pepe', 30)
persona4 = PersonaCons('María', 20)

persona3.mostrar_datos()
persona4.mostrar_datos()

print(persona3)