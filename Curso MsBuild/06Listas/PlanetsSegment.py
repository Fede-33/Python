#Create a list of planets
#Ask the user to choose a planet
#Display the planets that are closer and further to the sun, considering the chosen planet
#The program must not be key sensitive

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
choice = input("Write the name of a planet of the solar system: ").capitalize()
print("You choose planet", choice)
print(planets[0:planets.index(choice)], "are closer to the sun.")
print(planets[planets.index(choice)+1:], "are further to the sun.")