n = int(input('Enter the no of rows ypu want in your ster pattern :'))
a = int(input('Enter in which way you want your pattern (1-Ascending order  0-Descending order) : '))

if a ==1 or a==0 :
	

	if a==1 :
		for i in range(n):
			print(' * ' * (i+1))
			
	else :
		for i in range(n):
			print(' * ' * (n-i))
			
else : 
	print('choose correct option')
		
