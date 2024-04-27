# Ask the user to insert two distances from the sun, and calculate the distance between them

planet1 = int(input("Insert the first planet's distance from the sun: "))
planet2 = int(input("Insert the second planet's distance from the sun: "))

dist = abs(planet1 - planet2)

print ("The distance between planets is:", dist)