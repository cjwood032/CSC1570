# repeating_squares_Wood
# This program will get the turtle to draw squares
# Programmer: Christopher Wood
# date 2/09/18
# file name repeating_squares_Wood.py
# pseudocode
#1. create the turtle
#2. move the turtle to the starting drawing position
#3. draw the first line of the square
#4. turn left
#5. draw the second line of the
#4 repeat the square drawing increasing the size by 1 for 100 times.

import turtle #create the turtle
length=0 #create the turtle
turtle.penup() #create the turtle
turtle.goto(100,-100) #move the turtle to the starting drawing position
turtle.pendown()
turtle.hideturtle()
turtle.speed(0)
turtle.left(90)
turtle.pensize(2)
while length<500:
    length=(5+length)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
