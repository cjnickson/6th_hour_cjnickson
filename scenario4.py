#Name: CJ Nickson
#Class: 6th Hour
#Assignment: Scenario 4
from HW13 import number

print("helloworld!")
#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

#Step 1. Establish Variables

#Step 2. Make a loop

#Step 2a. Ask for a rating number

#Step 2b. Check if rating number is between 1 and 5

#Step 2c. If rating number is valid, add to total

#Step 3. Find and print the average
playercount = int(input("insert number of players"))
ratingsum = 0
for i in range(1,playercount +1):

    ratingnumb = int(input("inser rating"))
    if ratingnumb > 5 or ratingnumb< 1:
        print("invalid number")
    else:
        ratingsum += ratingnumb

average = ratingsum / playercount
print(average)