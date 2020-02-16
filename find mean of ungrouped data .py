n = int(input('Of how many numbers you want to find mean :'))
sum = 0
for i in range (n):
	print('Input the ' , i+1, end='' )
	print( 'st number :' , end='' )
	num = int(input())
	sum += num
	
print ('mean of the given numbers is:' , (sum/n))


