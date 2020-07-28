def sleep_end():
	import time
	timpe.sleep(5)

def intro():
	print("\nWelcome to the Heath Management Program ! \nDeveloved by HAMMAD ALI ")
	print("In this program you can record your diet and exercise and can also view them when required. ")
	print("So lets get started!") 
	print("************PLEASE DONT USE SPACES WHILE TYPING**************")

def getdatetime():
	import datetime
	a = datetime.datetime.now()
	b = a.strftime('%d/%m/%y %H:%M:%S')
	return b

def update(x):
	with open(f"{clientname}{feature}.txt" , "a") as file:
		file.write(getdatetime())
		file.write(f"\t{x}\n")
		print ("Record updated successfully!\n")

def fetch():
	with open(f"{clientname}{feature}.txt") as file:
		print("")
		for line in file :
			print(line , end="")

if __name__ == '__main__':

	intro()
	clientname = input("\nTYPE your name (ONLY FIRST NAME) : \n")
	clientname = clientname.lower()
	previous_clients = []

	while True:

		feature = input(f"\n{clientname.upper()} TYPE on which you want to work (Diet or Exercise):\n")
		feature = feature.lower()
		feature_list = ["diet", "exercise"]
		while feature.lower() not in feature_list:
			print(f"\n{clientname.upper()} choose correct feature \n")
			feature= input(f"\n{clientname.upper()} TYPE on which you want to work (Diet or Exercise):\n")

		def final():

			task = input(f"\n{clientname.upper()} TYPE your option (Record or Fetch):\n")
			task = task.lower()

			if task == "record" :
				done_what = input(f"\n{clientname.upper()} What you want to add to your record :\n")
				update(done_what)
				previous_clients.append(clientname)
			elif task == "fetch":
				try:
					fetch()
				except Exception as error :
					print (f"\n{clientname.upper()} First add something to your record\n")
			else:
				print(f"\n{clientname.upper()} choose correct task\n")
				final()

		final()

		run_choice = input(f"{clientname.upper()} Do you want to run again (y/n)\n")
		run_choice.lower()
		if run_choice == "n" :
			print(f"\nEnjoyed working with you {clientname.upper()}\n Bye!")
			time.sleep_end()
			break
		elif run_choice == "y" :
			continue
		else :		
			print(f"\n{clientname.upper()} Choose correct option\n") 
			
