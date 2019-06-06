# compound interest
# this program will calculate the compound interest of money deposited into a bank
# Programmer: Christopher Wood
# date 1/25/18
# file name compound interest.py
# pseudocode
# 1. input the principal originally deposited into the account
# 2. input the annual interest rate
# 3. input the nunber of times per year the interest is compounded
# 4. input the number of years the account will be left to earn interest
# 5. calculate the amount of money in the account after the specified number of years
# 6. output the amount of money in the account

principal=float(input('how much money is being put in the account?')) # input the principal
interest =float(input('what is the annual interest rate?')) #input the interest rate
Interest=float(interest/100) #converting the percent value to decimal
compounded=float(input('how many times per year is the interest compounded?')) #input the number of times interest is compounded
time=int(input('how many years is the money being left in the account to earn interest?')) #input the number of years the account will be left
money= principal*((1+(Interest/compounded))**(compounded*time)) #calculate the amount of money in the account
print('there will be $', format(money,'.2f'), "after", time, "years.") #output the amount of money