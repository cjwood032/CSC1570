#unique_words_Wood
#this program checks a file and displays all the unique words
#programmer: Christopher Wood
#date: 4/12/18
#unique_words_Wood.py
#pseudocode
#1. create the set to be used
#2. prompt the user for the file name
#3. open the file
#4. add each line to the set
#5. once the set is full, output all the items in the set.



wordset=set() #create the set
file=str(input("Enter the name of the file you would like to process:\n")) #prompt the user for the file name
Words_file = open(file, "r") #open the file in read mode
Line=Words_file.readline().strip().split() #read the first line
while str(Line) != "[]": #loop runs until an empty value is returned
	Line=str(Line[0]) #converting the Line variable to a immutable type
	wordset.add(Line) #add the word to the set
	Line=Words_file.readline().strip().split() #read the next line

print('The list of unique words are as follows.') #output
for word in wordset: #iterate over the set
	print(word) #print the unique word
