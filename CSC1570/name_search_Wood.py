#name_search_Wood.py
#this program will compare names to lists of popular boys and girls names
#programmer: Christopher Wood
#Date: 5/09/18
#name_search_Wood.py
#pseudocode
#1. User inputs a girl's or boy's name
#2. open the appropriate file for the gender
#3. compare the name to each name
#4. test if the name is in the file
#5. output whether or not the name was found.
def main():
    user_name=str(input("Enter a girl's name, or 'N' if you do not want to enter a girl's name: ")) #user inputs a girl name
    if user_name !="N": #if user enters a name
        girl_check(girl_name=user_name) #runs the girl_check method
    else:
        user_name = str(input("Enter a boys's name, or 'N' if you do not want to enter a boy's name: ")) #user inputs a boy name
        if user_name !='N': #if user enters the name
            boy_check(boy_name=user_name) #run boy_check method
        else: main() #if they didn't want to enter either a boy or girls name go back to the main method
def girl_check(girl_name): #define the method girl check
    name_list=[]
    Names = open('GirlNames.txt', 'r') #open the appropriate file
    searchgirls = Names.readline()    #Read the first name in the list.
    while searchgirls != '': #Read the rest of the file.
        searchednames = searchgirls.rstrip('\n')     #Strip \n from the names
        name_list.append(searchednames)
        searchgirls = Names.readline() #Read the next name in the file.
    if girl_name in name_list: #if the name wasn't found
        print(girl_name, 'is one of the most popular girl\'s names.') #print that the name is popular
    else: print(girl_name, 'is not one of the most popular girl\'s names.') #print that the name isn't popular
def boy_check(boy_name): #define the method boy check
    name_list = []
    Names = open('BoyNames.txt', 'r')  # open the appropriate file
    searchboys = Names.readline()  # Read the first name in the list.
    while searchboys != '':  # Read the rest of the file.
        searchednames = searchboys.rstrip('\n')  # Strip \n from the names
        name_list.append(searchednames)
        searchboys = Names.readline()  # Read the next name in the file.
    if boy_name in name_list:  # if the name wasn't found
        print(boy_name, 'is one of the most popular boy\'s names.')  # print that the name is popular
    else:
        print(boy_name, 'is not one of the most popular boy\'s names.')  # print that the name isn't popular
main()