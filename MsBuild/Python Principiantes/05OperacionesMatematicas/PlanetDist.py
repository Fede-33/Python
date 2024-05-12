#You are giver two distances of two planets from the sun (km), 
#and you have to calculate the distance between them 
#the distance have to be expressed in km and in miles (1 km = 1.609344 mi)

planet1 = 149597870
planet2 = 778547200

dist = planet2 - planet1

print ("The distance is:")
print (dist,"km")
print (dist / 1.609344, "mi")

