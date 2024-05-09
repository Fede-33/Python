# Create a function that shows the name and age of an uncertain amount of people
# Call the function with invented arguments

def ages(**kwargs):
	for indice in kwargs.keys():
		print(f'Name: {indice} / Age: {kwargs[indice]}')

ages(Juan = 20, Tom = 25, Anna = 22, Nick = 18) 