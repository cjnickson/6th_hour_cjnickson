#Name: CJ Nickson
#Class: 6th Hour
#Assignment: HW16

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
import random
from random import choices


def play_rps():
    user_choice = int(input("enter 1: for rock, 2: for papper,3: for scissors:"))
opponent_choice=random.randint(1,3)
choices = {1: "rock",2: "papper",3:"scissors"}
print(f"you chose:{choices[user_choice]}")
print(f"opponent chose:{choices[opponent_choice]}")
if user_choice == opponent_choice: return "its a tie!"
elif (user_choice == 1 and opponent_choice ==3) or/
(user_choice==2 and opponent_choice==1)or/
(user_choice==3 and opponent_choice==2):
return "you win!"
else
return "you lose!"


#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
replayinput = ("would like to play again? yn")
def play_repeat():
    if replayinput =="y":
        rock_paper_scissors()
    elif replayinput =="n"
exit()
    