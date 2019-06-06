#golf_scores_Wood.py
# this program will keep track of golf scores
# Programmer: Christopher Wood
# date 3/22/18
# file name golf_scores_Wood.py
# pseudocode
#1. Ask the user if they would like to enter scores or see scores
#For entering scores
#1. Ask the user if they want to append or rewrite the file
#2. Open the file based on the user's selection
#3. Prompt the user for the number of players
#4. for each player, prompt the user for the player's name and their score
#5. write each name/score set into the file
#6. close the file
#7. ask the user if they would like to take any additional actions
#8. call the main function if they select yes
#For reading scores
#1. open the file in read mode
#2. For each line, read it
#3. print the pleyr and their score
#4. once all the name/scores are displayed, close the file
#5. ask the user if they would like to take any additional actions
#6. call the main function if they selected yes
def main():
	print('Which action would you like to perform?\n','\t1. Enter scores\n','\t2. See the entered scores\n')#menu
	option=int(input('Option number:'))#user enters choice
	if option == 1: #user chooses option "1" for writing
		Writing_file()
	elif option == 2: #user chooses option "2" for reading
		Reading_file()
	else: #user did not enter a correct choice
		print('/nonly enter a number, either 1 or 2.') #remind user of correct choice
		main() #loop back to beginning
def Writing_file(): #writing the file
	golf=str('Golf.txt') #set the file that will be written
	W_option= None #create the variable for writing option
	while W_option != 'add' and W_option != 'erase': #set a loop if the user enters an incorrect option
		print('Would you like to add to existing scores, or erase the old scores?') #ask the user which option they would like
		W_option=str(input('type add to add, or erase to erase:')) #get the user input
		if W_option=='add': #if user chooses "add" option
			Scores_file = open(golf, "a") #file is opened in append mode
		elif W_option == 'erase': #user chooses "erase" option
			Scores_file = open(golf, "w") #open file in write mode
		else: #user chose the wrong option
			print('either type “add” or “erase” without quotes for proper option choice') #inform the user of the proper choisce
	Number_players=int(input('How many players were in the tournament?')) #get input for the number of players to add
	iter=1 #set the player loop count to 1
	while iter <= Number_players: #loop repeats until all players are entered
		Player_name=str(input('Enter the name of the player:')) #get the name of the player
		print('Enter', Player_name, end="") #get the player's score
		print("\'s", end=' ') #get the player's score
		Player_score=str(input('score:')) #user inputs score
		Comb_player=(Player_name +' ' + Player_score) #combine the player and the score as one variable
		Scores_file.write(Comb_player + '\n') #write the combined name/score in the file
		iter+=1 #increase the loop count
	Scores_file.close() #close the file when done writing
	ADD_act=str(input('Would you like to perform another action? \n y/n: ')) #prompt the user if they want to do more
	if ADD_act== 'y': #if user selects "y" to restart
		main() #call the main function
	else: #if user types anything else
		print('Goodbye.') #they have selected no

def Reading_file(): #define ther reading file function
	golf=str('Golf.txt') #set the file variable
	Scores_file = open(golf, "r") #open the file in read mode
	Line=Scores_file.readline().strip().split() #read the first line
	while str(Line) != "[]": #set a while loop for as long as each line has information
		(Player_name, Player_score) = Line #get the two values from the Line variable
		print('Name:', Player_name,'\nScore:',Player_score) #print the player's name and score
		Line=Scores_file.readline().strip().split() #read the next line
	Scores_file.close() #close the file when done reading
	ADD_act=str(input('Would you like to perform another action? \n y/n: ')) #prompt the user if they would like to do more
	if ADD_act== 'y': #if the user selects "y" to restart
		main() #call the main function
	else: print('Goodbye.') #they have selected no
		
main() #call the main function
