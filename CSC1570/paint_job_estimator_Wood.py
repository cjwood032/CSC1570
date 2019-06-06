# paint_job_estimator_Wood
# This program will calculate the cost of painting a wall
# Programmer: Christopher Wood
# date 2/20/18
# file name paint_job_estimator_Wood.py
# pseudocode
#user inputs the area of the wall
#divide the area of the wall by 112, rounding up to get the gallons of paint
#user inputs the price per gallon
#multiply the gallons of paint by 8 to get the number of hours worked
#multiply the gallons of paint by the price of a single gallon paint for the paint cost
#display the total hours of labor required for the paint job
#multiply the hours worked by 35 for the labor costs
#the total cost will be the paint charges plus labor charges
#display the gallons of paint, paint charges, labor charges, and total cost to the user

def main():
    area=float(input("How much wall will be painted (in square feet)?")) #user inputs the area of the wall
    gal=gallons(area)#run the gallons function
    paint_cost=Paint_cost(gal)#display the number of gallons of paint required
    hours=gal*8 #multiply the gallons of paint by 8 to get the number of hours worked
    print("hours of labor:", hours)  # display the number of hours of labor required
    labor_cost=Labor_cost(hours) # run the labor function
    total_cost=paint_cost+labor_cost #The total cost will be the paint charges plus the labor charges
    print("Total charges: $", end='') #Display the total cost to the user
    print(format(total_cost,",.2f")) #Display the total cost to the user

def gallons(area):
    gal=area/112#divide the area by 112
    if gal != area// 112 or area//112 == 0:  # if there is a remainder, add 1 more number of gallons required
        gal += 1
    gal=int(gal)#Make sure there's no remainder
    return gal

def Paint_cost(gal):
    paint_price = float(input("What is the price per gallon for paint?")) #user inputs the price for gallon
    print("Gallons of paint:", gal) #display the price per unit
    paint_cost = gal * paint_price #multiply the gallons of paint by the price per gallon of the paint to get total paint cost
    print("paint charges: $",end='') #display the paint charges
    print(format(paint_cost,",.2f"))
    return paint_cost

def Labor_cost(hours):
    labor_cost=hours*35#multiply the hours worked by 35 for the labor costs
    print("Labor charges: $",end='')#display the labor cost
    print(format(labor_cost,",.2f"))#display the labor cost
    return labor_cost

main() #run the main function.