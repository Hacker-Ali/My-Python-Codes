operator = input("which operator u want to use")
a = int(input("enter 1 no"))
b =int( input("enter 2 no"))

if operator == "+" :
	if a == 56 and b == 9 :
		print ('result is' , 77)
	else :
		print (a+b)

elif operator == "*" :
	if a == 45 and b == 3 :
		print ('result is' , 555)
	else :
		print (a*b)

elif operator == "/" :
	if a == 56 and b == 6 :
		print ('result is' , 4)
	else :
		print (a/b)
		
elif operator == "-" :
		print ("result is" , a-b)
		
else :
		print ("choose valid operator")
		

