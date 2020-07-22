n = 18
guesses_available = 9

while 1 :

	if guesses_available > 0 :
		guessed_no = int(input("guess a no:"))
	
   	if guessed_no > n :
			print("your no is greater")
			guesses_available -= 1
			print ("no of guesses left :" , guesses_available)

		elif guessed_no < n :
			print("your no is smaller")
			guesses_available -= 1
			print ("no of guesses left :" , guesses_available)
			
		else guessed_no == n:
			print("you won")
			print ("no of guesses taken:" , 9-guesses_available)
			break
			
	elif guesses_available == 0 :
		print ('you loss')
		break
		
	else :
		print('unexpected error')
		break
	
				
			
			
			
		