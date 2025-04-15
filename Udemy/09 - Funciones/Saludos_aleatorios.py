import random

def hello(nombre:str):
    print(f'Buenos días {nombre}')

def hellos (nombres:list):
    for nombre in nombres:
        print(f'Buenos días {nombre}')

def random_format(nombres:list, saludos:list):
    print(f'{saludos[random.randint(0,9)]}, {nombres[random.randint(0,9)]}')

nombres = ["Ana", "Juan", "Sofía", "Mateo", "Isabella", "Lucas", "Valentina", "Benjamín", "Camila", "Santiago"]

saludos = ["Hola", "Buenos días", "Buenas tardes", "Buenas noches", "¿Qué tal?", "Un gusto saludarte", "Encantado/a de conocerte", "¡Aló!", "¿Cómo estás?", "Saludos cordiales"]

hello('Pepe')
hellos (nombres)
random_format(nombres, saludos)