# hot_dog_cookout_Wood
# this program will calculate the leftovers from a cookout
# Programmer: Christopher Wood
# date 2/14/18
# file name hot_dog_cookout_Wood.py
# pseudocode
# Get the number of attendees
# Get the number of hot dogs for each person
# Calculate the total number of hot dogs required
#	Number of attendees * the total number of hot dogs= number of hots required
# Calculate the number of packages of hot dogs that are required (10 dogs per package)
#display the number of packages of hot dogs that are needed
#	Number of hots required/10=number of hot packages required
#	if there is a remainder, add 1 more package to the packages required
#Calculate the number of hot dogs remaining
#	number of hots packages * 10 – number of hots required = the remaining dogs
# Calculate the number of packages of buns that are required (8 buns per package)
#	Number of buns required/8=number of bun packages required
#	if there is a remainder, add 1 more package to the packages required
#Calculate the number of buns remaining
#	number of bun packages *8 – number of buns required = the remaining buns
#Display the remaining hot dogs and buns

attendees=int(input("Enter the number of attendees for the cookout:\n"))# Get the number of attendees
dogspp=int(input("Enter the number of hot dogs each person will eat:\n"))# Get the number of hot dogs for each person

dogs_needed=int(attendees*dogspp)# Calculate the number of packages of hot dogs that are required (10 dogs per package)
dogs_pax=dogs_needed//10#	Number of hots required/10=number of hot packages required
if dogs_pax!=dogs_needed/10 or dogs_pax==0:#	if there is a remainder, add 1 more package to the packages required
    dogs_pax+=1#	if there is a remainder, add 1 more package to the packages required
dog_rem=dogs_pax*10-dogs_needed#Calculate the number of hot dogs remaining
print("Minimum packages of hot dogs required:",dogs_pax) #Display the number of packages of hot dogs needed

bun_pax=dogs_needed//8#	Number of buns required/8=number of bun packages required
if bun_pax!=dogs_needed/8 or bun_pax==0:#	if there is a remainder, add 1 more package to the packages required
    bun_pax+=1#	if there is a remainder, add 1 more package to the packages required
bun_rem=bun_pax*8-dogs_needed#Calculate the number of buns remaining
print("Minimum packages of buns required:",bun_pax) #Display the number of packages of buns needed
print("\n\nThere will be",dog_rem,"hot dogs\n and",bun_rem,"buns left over.")#Display the remaining hot dogs and buns
