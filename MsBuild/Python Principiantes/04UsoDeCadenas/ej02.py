# Crear tres variables con los siguientes valores name(Ganymede), planet(Mars), gravity(1.43)

name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'

#Crear un template para darle formato a la información que mostraremos, deberá verse así:
#Gravity Facts about {name}
#--------------------------
#Planet Name: {planet}
#Gravity on {name}: {gravity} m/s2

template = """Gravity Facts about {name}
----------------------------------------
Planet Name {planet}
Gravity on {name}: {gravity} m/s2"""

#Usar el Template para mostrar los datos ingresados

print(template.format(name=name, planet=planet, gravity=gravity))
