#Your goal is to create a function that removes the first and last letters of a string. 
#Strings with two characters or less are considered invalid.
#You can choose to have your function return null or simply ignore.


string="abcdefg hijk"

if(len(string)<2):
	print(f'El string es invalido, tiene {len(string)} caracter/es') 
else:
	strip_string = string[1:-1]

print(f"El nuevo string es: {strip_string}")