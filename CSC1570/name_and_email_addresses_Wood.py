#name_and_email_addresses_Wood.py
#this program will compare names to lists of popular boys and girls names
#programmer: Christopher Wood
#Date: 5/09/18
#name_and_email_addresses_Wood.py
#pseudocode
#1. import the pickle method
#2. define the choices
#3. create a blank emails list
#4. Have each menu option go to a different method
#5. Methods
#Method 1 - Look up
    #1. open the emails.dat file
    #2. user inputs a name
    #3. method outputs name/email pair or if the email is not found.
#Method 2 - Add
    #1. User inputs name
    #2. User inputs email
    #3. Method checks if name/email pair already exists
    #4. Method creates pair if it doesn't already exist.
#Method 3 - Change
    #1. user inputs name
    #2. open the emails.dat file
    #3. record the old email address
    #4. user inputs new email address
    #5. display name and what the email was changed to.
#Method 4 - Delete
    #1. open the emails.dat file
    #2. user inputs name
    #3. copy address name
    #4. Delete pair
    #5. display what was deleted.
#Method 5 - Exit
    #1. exit
import pickle #open the pickle
LOOK_UP = 1 #Set choice 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    emails = pickle.load(open('emails.dat', 'rb'))  # open the emails.dat file
    choice = 0
    while choice != QUIT:
        choice = getMenuChoice()
        if choice == LOOK_UP:
            lookUp(emails)
        elif choice == ADD:
            add(emails)
        elif choice == CHANGE:
            change(emails)
        elif choice == DELETE:
            delete(emails)
        else:
            exit

def getMenuChoice():
    print()
    print('\t\tMenu')
    print('|---------------------------------------|')
    print('|1. Look up an email address\t\t\t|')
    print('|2. Add a new name and email address\t|')
    print('|3. Change an existing email address\t|')
    print('|4. Delete a name and email address\t\t|')
    print('|5. Quit the program\t\t\t\t\t|')
    print('|---------------------------------------|')

    choice = int(input('Enter the choice: '))
    while choice < LOOK_UP or choice > QUIT: #if they do not select a proper option
        choice = int(input('Please enter a valid choice: ')) #prompt them to input a proper choice

    return choice

def lookUp(emails): #look up emails function
    emails = pickle.load(open('emails.dat', 'rb')) #open the emails.dat file
    name = input('Enter a name: ') #prompt the user for a name
    print(emails.get(name, 'Sorry, that name is not found.')) #output the name, or if the name was not found
    input() #pause
def add(emails): #add emails function
    name = input('Enter a name: ') #prompt the user for a name input
    email_address = input('Enter an email address: ') #prompt the user for an address
    if name not in emails: #if the name isn't already engtered
        emails[name] = email_address #create the value for the pair
        pickle.dump(emails, open("emails.dat", "wb"))#pickle the file
        print(name, "\n", email_address, "\n added to directory")#output the verification
        input() #pause
    else:#if the name/email pair already exists
        print('Entry already exists.')#inform user entry already exists
        input() #pause
def change(emails): #define the change emails function
    name = input('Enter a name: ') #prompt the user to input a name
    emails = pickle.load(open('emails.dat', 'rb'))  # open the emails.dat file
    if name in emails: #check if it is a valid name
        oldaddress=emails.get(name)#get the old address
        address = input('Enter the new address: ') #prompt the user for the new email address
        emails[name] = address #save the new address
        pickle.dump(emails, open("emails.dat", "wb"))#save the new file
        print(name, "\n", oldaddress, "changed to:", address) #output the verification
        input()#pause
    else:#if the name is not found
        print('That name is not found.') #output the name is not found

def delete(emails): #delete emails function
    emails = pickle.load(open('emails.dat', 'rb'))  # open the emails.dat file
    name = input('Enter a name: ') #prompt the user which name to delete
    if name in emails: #if the name is in the emails
        address=emails.get(name)
        del emails[name] #delete the name
        print(name, address "has been removed from the directory") # ouptut the verificaiton
        input() #pause
    else: #if the name is not found
        print('Sorry, that name is not found.')#output the name is not found.

main()