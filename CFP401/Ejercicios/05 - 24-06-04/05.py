# Dado el siguiente diccionario:
#personas = [
# {"nombre": "Juan", "edad": 25},
# {"nombre": "María", "edad": 30},
# {"nombre": "Carlos", "edad": 28},
# {"nombre": "Ana", "edad": 22} 
#]
#liste los nombres y edad de cada una de las personas. En este caso tiene que iterar toda la colección, ¿qué estructura utilizaría?

personas = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 30},
    {"nombre": "Carlos", "edad": 28},
    {"nombre": "Ana", "edad": 22} 
]
for i in personas:
    print(f"{i['nombre']} tiene {i['edad']} años.")