# Create a function that shows the name and age of an uncertain amount of people
# Ask the user to input the desired names
# Call the function 

def ages(kwargs):
	for indice in kwargs.keys():
		print(f'Name: {indice} / Age: {kwargs[indice]}')

num = int(input("How many dames and ages? "))
members = {}

while num != 0 :
	name = input("Name: ")
	members [name] = int(input("Age: "))
	num -= 1

ages(members) 