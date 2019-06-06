# drivers_license_exam_fixed_Wood
# this program will a student's driver's exam score
# Programmer: Christopher Wood
# date 3/7/18
# file name drivers_license_exam_Wood.py
#pseudocode
#1. Generate the correct answer list
#2. Open the student’s answers file
#3. Import the student’s answer file into a list
#4. Compare each answer, one at a time
#5. Keep a running total of number of incorrect answers.
#6. If the number of incorrect answers is 5 or more, the student failed
#7. Output if the student passed or failed
#8. Output the number of correct answers
#9. Output the number of incorrect answers
#10. Close the file
def main():
    A = str("A")
    B = str("B")
    C = str("C")
    D = str("D")
    answer_key=[A,C,A,A,D,B,C,A,C,B,A,D,C,A,D,C,B,B,D,A] #generate the correct answer list
    user_file = input("Enter the name of the file:")  # prompt the user for the file name
    wrong_total=student(file=user_file,key=answer_key)#create the user list
    if wrong_total>=5: #Output if the student passed or failed
        print("You Failed")
    else: print("You Passed!")
    right_total=20-wrong_total
    print("You got:",wrong_total,"wrong.\n")#output the number of incorrect answers
    print("You got:",right_total,"correct.")#output the number of correct answers


def student(file,key):
    student_answers = open(file, 'r')  # open the file
    number=0
    total_wrong=0
    Number=0
    student_list =student_answers.readlines() # create the list
    for item in student_list:
        increment=answer_check(Student_list=student_list, question_number=Number,answer_list=key)
        total_wrong+=increment
        Number+=1
    student_answers.close() #close the files
    return total_wrong#return the total numbers of incorrect answers

def answer_check(Student_list, question_number, answer_list): #function to check answer
    add_wrong=0 #reset the variable
    correct_answer=str(answer_list[question_number])#get the correct answer
    student_answer = str(Student_list[question_number].strip("\n"))  # get the correct answer
    if student_answer != correct_answer:#compare the two answers
        add_wrong=1 #if wrong will add 1 more to the total of wrong answers
    print(student_answer)#output the student's response
    return add_wrong#return if the value is false

main() #run the main function