# You will use the same threshold for size of 5m3. If the object is both larger than the threshold and within 1000km of the ship evasive maneuvers will be required.

object_size = float (input ("Input object size: "))
prox = float (input ("Input proximity distance: "))

if (object_size > 5 and prox < 1000) :
    print ('Evasive maneuvers required')
else :
    print ('Object poses no threat')