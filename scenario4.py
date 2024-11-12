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
total_ratings = 0
number_of_players = int(input("enter the number of players:"))
#Step 2. Make a loop
for i in range(number_of_players):
#Step 2a. Ask for a rating number
ratingsum = int(input(f"enter rating for player{i+1}:"))
#Step 2b. Check if rating number is between 1 and 5
while ratingsum< 1 or ratingsum>5
    print("invalid rating. please enter a rating between 1 and 5.")
    ratingsum = int(input(f"enter rating for player {i+1}:"))
#Step 2c. If rating number is valid, add to total
total_ratings += ratingrum
#Step 3. Find and print the average
average_rating = total_ratings/ number_of_players
print(f"the average rating is:{average_rating}")