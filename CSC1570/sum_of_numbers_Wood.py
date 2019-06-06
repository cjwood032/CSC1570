# sum_of_numbers_Wood
# this program will calculate the the sum of positive entered by the user
# Programmer: Christopher Wood
# date 2/09/18
# sum_of_numbers_Wood.py
# pseudocode
#1. Set the loop up
#2. prompt the user to enter a number
#3. upon ending the loop, add up all the positive numbers
integer=0
sum=0
while integer>=0: #set up the loop
    integer=int(input("enter a positive number, or a negative number to get the sum and exit:"))
    if integer>=0:
        sum=(sum+integer)
print("\n\n\nTotal=",sum)