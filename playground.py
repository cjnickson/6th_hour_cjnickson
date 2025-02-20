#name CJ Nickson
#class 6th hour
#assigment playground


print("helloworld")

numlist = [88,89,35,33,20,23,5,1]
numlist.sort()
print(numlist)

input("what is your name")

x=int(input('give me 1 integer'))
y=int(input('give me another integer'))
z=x+y
print(z)

classlist=["CJ", "cy","raji","tyson","wald","kashen","tate","ethan","nate","forby"]
classlist.append(input())
print(f"{classlist[0]} is HERE!")
print(classlist)

print(" Weatherford beats kingfisher 28-0")

numbers = [77,55,45,6,9,2]
print(numbers)
sum = numbers[0] + numlist[3]
print(sum)

import random

def guess_number():
    number_to_guess= random.randint(1,100)
    guess = None

    print("Welcome to the number guessing game!")

    while guess != number_to_guess:
        guess= int(input("guess a number between 1 and 100:"))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("too high! try again.")
    else:
      print("congratulation! you guessed it!")

    guess_number()