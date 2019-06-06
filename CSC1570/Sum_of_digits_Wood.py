# Sum of Digits
# this program will calculate the sum of the digits of a string of single digit numbers
# Programmer: Christopher Wood
# date 3/14/18
# file name Sum_of_digits_Wood.py
# pseudocode
#1. prompt the user to enter a string comprising only of numbers
#2. Create a loop that will read each digit from the string
#3. Add each digit to the total
#4. When there are no more digits left in the string, return the total
user_string=str(input("Enter a sequence of numerical digits with nothing separating them:")) #user enters string
numlen = 0 #create variables
total = 0 #create variables
iterations = len(user_string) #set the number of iterations the loop will run
while numlen < iterations: #define the loop
    digit = user_string[numlen] #read each digit
    total += int(digit)#add the read digit to the total
    numlen += 1 #set up for the next iteration
print("The total in the string you entered is") #return the total
print(format(total, "^20.0f")) #return the total


