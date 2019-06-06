#emp_wood (part of test_Wood.py)
#this program creates a class to be called by test_Wood.py
#programmer: Christopher Wood
#Date: 4/28/18
#emp_Wood.py
#pseudocode
#1. create the appropriate class
#2. call the init method
#3. create the mutator and accessor methods for the employee's name and number

class Employee: #create the Employee class

    def __init__(self,name,number): #call the init method
        self.__name = name #create the employee's name'
        self.number = number#create the employee number
    def set_employee_name(self,name): #create mutator for name
        self.__name = name
    def set_employee_number(self,number): #create mutator for number
        self.__number = number
    def get_employee_name(self):# create accessor for name
        return self.__name
    def get_employee_number(self): #create accessor for number
        return self.number