#pet_driver_Wood
#this program creates a class for storing the information on a pet
#Programmer: Christopher Wood
#4/20/18
#program name: pet_driver_Wood.py
#psuedocode
#1. create the pet class
#2. set the init method
#3. define self. and get. for name, type, and age
#4. create a function that will prompt the user to input the pet's name, type, and age.
#5. call the Pet class using the user entered data.
#6. output the pet's name, type, and age

class Pet(object):  #create the pet class
    def __init__(self, name, animal_type, age): #initialize the pet class
        self.__name = name #create the name
        self.__animal_type = animal_type #create the animal type
        self.__age = age #create the age
#define the "set_" methods
    def set_name(self, name): #name
        self.__name = name
    def set_animal_type(self, animal_type): #type
        self.__animal_type = animal_type
    def set_age(self, age): #age
        self.__age = age
#define the "get_" methods
    def get_name(self): #name
        return self.__name
    def get_animal_type(self): #type
        return self.__animal_type
    def get_age(self): #age
        return self.__age

def main():
    name = input('Enter the name of the pet: ') #user inputs pet's name
    animal_type = input('Enter the type of animal: ')# user inputs pet's type
    age = int(input('Enter the age of the pet: ')) #user inputs pet's age
    pets = Pet(name, animal_type, age) #call the Pet class
    #output the pet's name, type, and age
    print('\n\nHere is the data you entered:')
    print('Pet Name: ', pets.get_name())
    print('Animal Type:', pets.get_animal_type())
    print('Age of pet: ', pets.get_age())

main()
