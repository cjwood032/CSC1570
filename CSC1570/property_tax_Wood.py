# property_tax_Wood
# This program will calculate the property tax of a property
# Programmer: Christopher Wood
# date 2/20/18
# file name property_tax_Wood.py
# pseudocode
#define the functions assessment and taxing
#Get the actual value of the property
#Calculate the assessed value, 60% of the actual value
#calculate the propery tax, for each $100 of the actual value add .72
#display the assessed value and the property tax

def main():
    assessed=assessment(percent=.6) #set the values for the percent and the cost for tax
    taxing(assessed,tax_cost=.72)
def assessment(percent):
    actual = float(input("enter the actual value of the property:"))  # get the actual value of the property
    assessed = percent * actual  # calculate the assessed value
    print("Assessed value: $",end='')# display the assessed value
    print(format(assessed, ",.2f"), "\n")  # display the assessed value
    return assessed
def taxing(assessed,tax_cost):
    tax = (assessed // 100) * tax_cost  # calculate the property tax, for each $100 of the assessed
    print("Property Tax: $",end='') # display the property tax
    print(format(tax, ",.2f"))  # display the property tax
    return tax
main() #run the main function
