import random 
import time 
print ("\t\t\t\t\t\t\t\t\t----[Stone Paper Scissors Game]---- ")

player_name = input("What is your  name :\n------->")	
rounds = int(input("\nHow many rounds you want to play:\n------->"))
player_score = 0
bot_score = 0

def scores():
	print (f"Computer's score : {bot_score}")
	print (f"{player_name}'s score : {player_score}")


for i in range(rounds):
	time.sleep(2)
	print("******************************************************************************************************************")
	print(f"ROUND - {i+1}")
	bot_choice = random.choice([1, 2, 3])
	player_choice = int(input("Choose any one:\n\t[1]Stone\n\t[2]Paper\n\t[3]Scissors\n------->"))
	time.sleep(1)

	if bot_choice == 1 and player_choice == 2 :
		print("Computer's choice : Stone")
		player_score += 1
		print(f"{player_name} wins")
		scores()

	elif bot_choice == 1 and player_choice == 3 :
		print("Computer's choice : Stone")
		bot_score += 1
		print("Computer wins")
		scores()

	elif bot_choice == 2 and player_choice == 1 :
		print("Computer's choice : Paper")
		bot_score += 1		
		print("Computer wins")
		scores()

	elif bot_choice == 2 and player_choice == 3 :
		print("Computer's choice : Paper")
		player_score += 1
		print(f"{player_name} wins")
		scores()

	elif bot_choice == 3 and player_choice == 2 :
		print("Computer's choice : Scissors")
		bot_score += 1
		print("Computer wins")
		scores()

	elif bot_choice == 3 and player_choice == 1 :
		print("Computer's choice : Scissors")
		player_score += 1
		print(f"{player_name} wins")
		scores()

	elif player_choice == bot_choice :
		print("Computer's choice is same as yours.")
		print("Tie")
		scores()

	else :
		print("Choose correct option")

time.sleep(2)
print("******************************************************************************************************************")
print ("Final scores are:")
time.sleep(5)
print("\t")
scores()

if player_score>bot_score :
	print (f"\t{player_name} WINS !")
	print ("\tComputer LOSES !")
	
elif bot_score>player_score :
	print("\tComputer WINS !")
	print (f"\t{player_name} LOSES !")

else :
	print ("\tMatch Tied !")

time.sleep(5)