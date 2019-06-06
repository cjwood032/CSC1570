#test.Wood.py
#this program uses pw_Wood.py and emp_Wood.py to
#programmer: Christopher Wood
#Date: 4/28/18
#test_Wood.py
#pseudocode
#1. import the ProductionWorker class
#2. Have user input the employee's information'
#3. call the ProductionWorker sublcass to process the input
#4. Output the employee's name, number, shift, and pay rate
def main():
	from pw_Wood import ProductionWorker #import ProductionWorker
	name = input('Enter the name: ') #user input's employee's name
	number = input('Enter the ID number: ') #user inputs employee ID number
	shift_num = input('Enter the shift number: ') #user inputs the shift number
	pay_rate = input('Enter the hourly pay rate: ') #user inputs the pay rate
	emp = ProductionWorker(name,number,shift_num,pay_rate) #run the production worker class

	print ('Production worker information:') #output the worker information
	print ('Name:',emp.get_employee_name()) #employee name
	print ('ID number:',emp.get_employee_number()) #employee ID number
	print ('Shift:',emp.get_shift_number()) #the employeed shift number
	print ('Hourly pay rate:',emp.get_pay_rate()) #the employee's pay rate

main()

