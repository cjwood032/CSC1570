#pw_wood (part of test_Wood.py)
#this program creates a sublclass from emp_Wood to be called by test_Wood.py
#programmer: Christopher Wood
#Date: 4/28/18
#pw_Wood.py
#pseudocode
#1. import the employee class
#2. create the appropriate class
#3. call the init method
#4. create the mutator and accessor methods for the employee's shift number and pay rate

from emp_Wood import Employee #import the employee class
class ProductionWorker(Employee): #create the sublass production worker

	def __init__(self,name,number,shift_number,pay_rate): #call the init method
       
		Employee.__init__(self,name,number) #initialize the employee class
		self.__shift_number = shift_number #create the shift number
		self.__pay_rate = pay_rate #create the pay rate
	def set_shift_number(self,shift_number): #create mutator for shift number
		self.__shift_number = shift_num
	def set_pay_rate(self,pay_rate): #create mutator for pay rate
		self.__pay_rate = pay
	def get_shift_number(self): #create accessor for shift number
		return self.__shift_number
	def get_pay_rate(self): #create accessor for pay rate
		return self.__pay_rate


