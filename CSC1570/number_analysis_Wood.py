# number_analysis_Wood
# This program will analyze a user-entered series of 5 numbers
# Programmer: Christopher Wood
# date 3/7/18
# file name number_analysis_Wood.py
# pseudocode
#1. Prompt the user to enter to enter the 5 numbers
#2. Save the inputs into a list
#3. Output the lowest number in the list
#4. Output the highest number in the list
#5. Total the numbers in the list
#6. Output the total
#7. Divide the total of the numbers by the length
#8. Output the average
def main(): #define the miain
    total=0
    value=0
    main_list=[]
    main_list=list_get()#prompt the user to enter the numbers
    print("\n\nlow:",min(main_list))#output the lowest number in the list
    print("high:",max(main_list))#output the highest number in the list
    for value in main_list: #total the numbers in the list
        total+=value
    average=total/len(main_list) #divide the total of the numbers by the length
    print("Average:",average) #output the average
def list_get():
    integer=1
    sub_list=[]
    while integer<=5: #loop to get a list of the first 5 numbers
        print("enter number",integer,end=' ') #prompt user for input
        user_number=int(input("of 5:")) #prompt user for input
        sub_list.append(user_number)
        integer+=1
    return sub_list

main()
