# money_counting_game_Wood
# this program will calculate if the user input the amount of change that adds up to a dollar
# Programmer: Christopher Wood
# date 2/16/18
# file name money_counting_game_Wood.py
# pseudocode
#Prompt the user to input the number of each coin they have
#Caclulate how much each set of coins is worth
#Add together the total value of each coin
#compare the total value to a dollar
print("\nMoney-counting game! Get the change to add up to $1 to win!\n\n\n")
p=int(input("enter the number of pennies\n"))#enter the number of pennies
n=int(input("enter the number of nickels\n"))#enter the number of nickels
d=int(input("enter the number of dimes\n"))#enter the number of dimes
q=int(input("enter the number of quarters\n"))#enter the number of quarters
vp=p*.01 #Calculate how much the pennies are worth
vn=n*.05 #Calculate how much the pennies are worth
vd=d*.1 #Calculate how much the pennies are worth
vq=q*.25 #Calculate how much the pennies are worth
value=vp+vn+vd+vq#Add together the total value of each coin
if value<1:#compare the total value to a dollar
    print("\nSorry, the amount you entered was less than $1")
elif value>1:#compare the total value to a dollar
    print("\nSorry, the amount you entered was more than $1")
else: print("\nthe amount you entered was exactly $1!\nYOU WIN THE GAME!")