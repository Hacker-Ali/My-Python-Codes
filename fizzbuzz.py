c = int ( input ( " How many nos you want to print : " ) ) 

for i in  range(c) :
 	i = i + 1

 	if ( i % 15 ) == 0 :
 		print ( " FizzBuzz " )

 	elif ( i % 5 ) == 0 :
 		print ( " Buzz " )

 	elif ( i % 3 ) == 0 :
 		print ( " Fizz " )

 	else :
 		print ( i ) 
