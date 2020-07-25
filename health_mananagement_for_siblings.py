# functions used
def intro():
	print("\nWelcome to the Heath Management Program ! \nDeveloved by HAMMAD ALI ")
	print("In this program you can record your diet and exercise and can also view them when required. ")
	print("So lets get started!") 
def getdatetime():
	""" This function will return current date and time """
	import datetime
	a = datetime.datetime.now()
	b = a.strftime('%d/%m/%y %H:%M:%S')
	return b
def client_name() :
	""" This function will return clients name """  
	c = int(input("Choose your name :\n [1]Irfan Ali \n [2]Hammad Ali \n [3]Suheb Ali \n "))
	return c
def feature():
	""" This function will return the feature that the client wants to use """
	d = int(input("Choose correct option : \n [1]Diet Recorder  \n [2]Exercise Recorder \n "))
	return d
def task():
	""" This function will return the task that the client wants to do """
	e = int(input("Choose your option : \n [1]Update Record \n [2]Fetch Record \n "))
	return e
def update():
	file.write("\n[")
	file.write(getdatetime())
	file.write("]\t")
	file.write(ate_what)
	print ("Record updated successfully!")
def fetch():
	for line in file :
		print(line , end="")

# intro
intro()

# main program
while True:
		
	# calling main functions
	clientname = client_name()
	varfeature = feature()
	vartask = task()

	# deit recorder  
	if varfeature == 1 :

		if clientname == 1 :
			if vartask == 1 :
				with open("irfandiet.txt" , "a") as file :
					ate_what = input("What you ate Irfan Ali : \n ")
					update()
			elif vartask == 2 :
				with open("irfandiet.txt") as file :
					fetch()
			else :
				print("Choose correct option")

		elif clientname == 2 :
			if vartask == 1 :
				with open("hammaddiet.txt" , "a") as file :
					ate_what = input("What you ate Hammad Ali : \n ")
					update()
			elif vartask == 2 :
				with open("hammaddiet.txt") as file :
					fetch()
			else :
				print("Choose correct option")

		elif clientname == 3 :
			if vartask == 1 :
				with open("suhebdiet.txt" , "a") as file :
					ate_what = input("What you ate Suheb Ali : \n ")
					update()
			elif vartask == 2 :
				with open("suhebdiet.txt") as file :
					fetch()
			else :
				print("Choose correct option")

		else :
			print("Choose correct name")

	# exercise recorder
	elif varfeature == 2:

		if clientname == 1 :
			if vartask == 1 :
				with open("irfanexercise.txt" , "a") as file :
					ate_what = input("What you did Irfan Ali : \n ")
					update()
			elif vartask == 2 :
				with open("irfanexercise.txt") as file :
					fetch()
			else :
				print("Choose correct option")

		elif clientname == 2 :
			if vartask == 1 :
				with open("hammadexercise.txt" , "a") as file :
					ate_what = input("What you did Hammad Ali : \n ")
					update()
			elif vartask == 2 :
				with open("hammadexercise.txt") as file :
					fetch()
			else :
				print("Choose correct option")

		elif clientname == 3 :
			if vartask == 1 :
				with open("suhebexercise.txt" , "a") as file :
					ate_what = input("What you did Suheb Ali : \n ")
					update()
			elif vartask == 2:
				with open("suhebexercise.txt") as file :
					fetch()
			else :
				print("Choose correct option")

		else :
			print("Choose correct name")

	# incorrect option handling
	else :
		print("Choose correct option")

	# exit confirmation
	run_choice = input("\nDo you want to run again (y/n)")
	run_choice.lower()
	if run_choice == "n" :
		print("Enjoyed working with you \n Bye!")
		break
	elif run_choice == "y" :
		continue
	else :
		print("Choose correct option") 















