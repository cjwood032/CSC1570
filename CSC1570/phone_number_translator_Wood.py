# phone number translator
# this program will translate a phone number from alphabetical characters to numerical
# Programmer: Christopher Wood
# date 3/14/18
# file name phone_number_translator_wood.py
# pseudocode
#1. prompt the user to enter a phone number
#2. Replace all letters with numbers
#3. Output the new phone number.


phone_number=str(input("Enter a phone number in the format XXX-XXX-XXXX:")) # user enters the phone number
phone_number = phone_number.replace("A", "2") #Replace the letter A
phone_number = phone_number.replace("B", "2") #Replace the letter B
phone_number = phone_number.replace("C", "2")#Replace the letter C
phone_number = phone_number.replace("D", "3")#Replace the letter D
phone_number = phone_number.replace("E", "3")#Replace the letter E
phone_number = phone_number.replace("F", "3")#Replace the letter F
phone_number = phone_number.replace("G", "4")#Replace the letter G
phone_number = phone_number.replace("H", "4")#Replace the letter H
phone_number = phone_number.replace("I", "4")#Replace the letter I
phone_number = phone_number.replace("J", "5")#Replace the letter J
phone_number = phone_number.replace("K", "5")#Replace the letter K
phone_number = phone_number.replace("L", "5")#Replace the letter L
phone_number = phone_number.replace("M", "6")#Replace the letter M
phone_number = phone_number.replace("N", "6")#Replace the letter N
phone_number = phone_number.replace("O", "6")#Replace the letter O
phone_number = phone_number.replace("P", "7")#Replace the letter P
phone_number = phone_number.replace("Q", "7")#Replace the letter Q
phone_number = phone_number.replace("R", "7")#Replace the letter R
phone_number = phone_number.replace("S", "7")#Replace the letter S
phone_number = phone_number.replace("T", "8")#Replace the letter T
phone_number = phone_number.replace("U", "8")#Replace the letter U
phone_number = phone_number.replace("V", "8")#Replace the letter V
phone_number = phone_number.replace("W", "9")#Replace the letter W
phone_number = phone_number.replace("X", "9")#Replace the letter X
phone_number = phone_number.replace("Y", "9")#Replace the letter Y
phone_number = phone_number.replace("Z", "9")#Replace the letter Z
print("the phone number is", phone_number) #Print the phone number as all numerals