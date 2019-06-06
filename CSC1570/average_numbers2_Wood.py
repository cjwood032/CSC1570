# average_numbers_Wood
# This program will open a file, and average the values in it
# Programmer: Christopher Wood
# date 2/28/18
# file name average_numbers_Wood.py
# pseudocode
#1. Prompt the user to give the file name
#2. open the file
#3. Read through the file, checking for any non-numeric data
#4. If there is non-numeric data, inform the user
#5. If there is only numeric data, import the data
#6. Compute an average of the numbers in the file
#7. Show the average.
#8. close the file

def main():
    total =0.0
    lines=0.0
    average=0.0
    try:
        user_file=input("Enter the name of the file:")#prompt the user for the file name
        num_file=open(user_file,'r')#open the file
        contents = num_file.read().strip().split()  # read the file's contents
        for numb in contents: #Compute the average of the numbers in the file
            amount = float(numb) #convert a string to a float
            total += amount #get the total
            lines += 1 #increase the counter
        average=total/lines #get the average
        print("The average is:",average) #show the average
        num_file.close() #close the file
    except IOError:#Input error exception
        print("an error occurred while trying to read the file, was the file's name entered correctly?")
    except ValueError: #value error exception
        print("Non-numeric data was found in the file.")
    except:#general error exception
        print("An error has occurred.")

main()
