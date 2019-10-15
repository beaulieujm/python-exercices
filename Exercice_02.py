# pratice-python exercice #2 
# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. More more

def convert_to_number(number) :
	try :
		nombre = int(number)
	except ValueError:
		print("Input is not a valid number.  Try again")
		nombre = "Not a number"
	return nombre
	
is_done = False	
while not is_done : 
	input_string  = input("Enter a number (q to exit) : ")
	if input_string == "q" :
		is_done = True
		break
	nombre = convert_to_number(input_string)
	if nombre != "Not a number" :
		if nombre%2 == 0 :
	  		parite = "pair"
		else :
	  		parite = "impair"    
		print("Le nombre " + repr(nombre) + " est " + parite + ".")

print("All done!")
exit() 

