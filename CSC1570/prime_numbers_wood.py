# prime_numbers_Wood
# This program will check if the numbers 1 through 100 are prime
# Programmer: Christopher Wood
# date 2/25/18
# file name prime_numbers_Wood.py
# pseudocode
# 1. define a function to check if a number is prime
# 2. for the numbers 1 through 100 use the function to check if the number is prime
# 3. If a number is not prime, you only have to check potential factors up to the squareroot of the number
# 3. because factor come in pairs, with one of the factors being less than the square root, and one being more.
# 4. Test all potential factors up to the square root of the number.
# 4a. If a potential factor is found, the number is not prime
# 5. if a number is not prime, the loop will exit

def main():
    for numero in range(1, 101): #run a loop of the first 100 digits
        is_prime(number=numero) #run the is_prime function


def is_prime(number): #the is_prime function definition
    squarert = number ** .5  # take the square root of the number to determine the range of potential factors
    int = 2 #start the count at 2, since every number is divisible by 1
    prime = True # the number is considered prime until it fails the prime test
    while int <= squarert and prime == True: #while loop to test all the possible factors, will stop count if number is not prime
        if number % int == 0: #if the number divided by the int has a remainder
            prime = False #the number is not prime
        int += 1 #increase the count
    if prime ==True: #if the number is prime
        print("The number", number, "is prime") #print the number is prime
    else: print("The number", number, "is not prime") #if the number is not prime, print that it is not prime

main() #call the main function
