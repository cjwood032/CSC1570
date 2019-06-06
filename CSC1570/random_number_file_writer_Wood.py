# random_number_file_writer_Wood
# This program will write a file with a user-specified number of random numbers ranging from 1-5000
# Programmer: Christopher Wood
# date 2/28/18
# file name random_number_file_writer_Wood.py
# pseudocode
#1. prompt the user to enter the file name and how many random numbers they want
#2. open the file
#3. write each additional random number to the file until enough numbers have been generated
#4. close the file
def main():
    user_file=str(input("Enter the name of the file to which results should be written:"))#user enters file name
    amount=int(input("Enter the number of random numbers to be written to the file"))#user enters how many numbers
    file=open(user_file,'w')#open the file
    loopcount=0
    while loopcount<amount:
        loopcount+=1
        value=randomize()
        file.write(str(value) + '\n')
    file.close()
def randomize():
    number = random.randint(1 , 5000)
    return number

import random
main()