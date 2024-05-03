#1 Create a dictionary containing the name and moons of the planet Mars. 
#2 Display the info with a string method
#3 Add the circumference info and display again with info updated 

#1
planet = {
    'name' : 'Mars',
    'moons' : 2
}
#2
print(f"The planet {planet['name']} has {planet['moons']} moons.")
#3
planet['circum'] = {
    'polar' : 6752,
    'equat' : 6792
}
print(f"The planet {planet['name']} has a polar circumference of {planet['circum']['polar']} Km, and an equatorial circumference of {planet['circum']['equat']} Km")
