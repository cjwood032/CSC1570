#course_information_Wood
#this program retains information for an individual's course list
#Programmer: Christopher Wood
#Date: 4/12/18
#course_information_Wood.py
#pseudocode
#1. set up the 3 dictionaries, for rooms, instructors, and times
#2. prompt the user to input the course number
#3. check to make sure the course is in the system
#4. get the room, instructor, and time from their rspective dictionaries for the course.
#5. Display the course information

Rooms= {'CS101' : '3004', 'CS102' : '4501', 'CS103':'6755', 'NT110': '1244', 'CM241' : '1411' } #define the rooms dictionary
Instructor= {'CS101' : 'Haynes', 'CS102' : 'Alvarado', 'CS103':'Rich', 'NT110': 'Burke', 'CM241' : 'Lee' } #define the instructor dictionary
Times= {'CS101' : '8:00 a.m.', 'CS102' : '9:00 a.m.', 'CS103':'10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241' : '1:00 p.m.' } #define the start times dictionary
course=str(input("Enter the course number: \t")) #prompt user for course name
while course not in Rooms: #inform user if their input was not found
	print('That is not a correct course number')
	print('please enter courses with all capital letters')
	course=str(input("Enter the course number"))
time=str(Times[course]) #get the start time for the input course 
room=str(Rooms[course]) #get the room for the input course
instructor=str(Instructor[course]) #get the instructor for the input course
print('\n\n','Course', course, 'meets at', time, 'in room', room, 'with', instructor, 'teaching') #print the course information.
