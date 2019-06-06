# Distance_traveled_Wood
# this program will calculate the distance traveled by a vehicle
# Programmer: Christopher Wood
# date 2/09/18
# file name distance_traveled_Wood.py
# pseudocode
#1. Prompt the user for the speed in mph
#2. Prompt the user for the hours it travelled
#3. calculate the total distance travelled for each hour.
#4. display the hours travelled

speed=int(input("How fast is the vehicle moving in MPH?"))#prompt the user for speed in MPH
hours=int(input("How many hours was the vehicle travel for?")) #prompt the user for number of hours the vehicle travelled
distance=0
hour=0
print("hours\t","|\t","distance travelled")
print("____________________________")
while hour<hours:
    hour = (hour+1)                  #calculate the total distance traveled for each hour
    distance = speed*hour
    print(hour,"\t\t|\t\t",distance) #display the hours travelled
