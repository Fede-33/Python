#Extract a list of information (name = age) and store it in a dictionary. 
#The info must come from another file that you created previously
#The external file must have two lines that does not match the desired format
#Use Exception control (ValueError) to extract the data despite of the unformatted lines


filedata = open('Extractinfo.txt', 'r') #Get the info from the file
dict = {} 

for line in filedata.read().split('\n'): #Read the info iterating on each line (split method)
	try:
		key, value = line.split('=') #assign key and value as the values separated by =
		dict[key] = value #assign to the dictionary
	except ValueError:
		print(f'Unable to read data from "{line}"')

print(dict) 