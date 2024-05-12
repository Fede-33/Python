#Create a variable list of the eight planets of the solar system:
#Display the planet's list
#Display the total number of planets
#Add Pluto to the list
#Display the new number of planets and the name of the last one

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The planets on the solar system are:", planets)
print("There are", len(planets), "planets in the solar system.")

planets.append("Pluto")
print("Prevously there were", len(planets), "in the solar system")
print("The last planet was", planets[-1])