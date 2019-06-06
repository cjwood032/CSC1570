#rec_Wood.py
#this program will create an asteriks drawing a number of times
#programmer: Christopher Wood
#Date: 5/03/18
#rec_Wood.py
#pseudocode
#1. create the variables
#2. Prompt the user for the number of times to recur
#3. print the asteriks

def main():
    ast='*' #create the string to print
    iterand=0
    times=int(input('How many lines would you like to draw?'))
    recur(ast,iterand,times)
def recur(ast,iterand,times):
    if iterand < times:
        print(ast)
        ast=ast+'*'
        iterand +=1
        recur(ast,iterand,times)
main()