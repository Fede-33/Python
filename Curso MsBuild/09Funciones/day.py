# Ask the user for an amount of hours and return how many days it will be (rounded)

def days(argu):
    return argu/24

hours = int(input('How many hours? '))

print (round(days(hours)))
