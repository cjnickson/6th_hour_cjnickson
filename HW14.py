#Name: CJ Nickson
#Class: 6th Hour
#Assignment: HW14
from math import factorial

#1. Create a variable that asks the user for an integer and an empty intger variable.
user_input = int(input("please eneter an integer:"))
#2. Create a loop with a range from 1 to the number the user input.
for i in range(1,user_input + 1):
    print(i)
#3. Use the loop to find the factorial of that number. A factorial of a number is that number multiplied
#by every number before it until you reach 1.
#For example: 5! is 5 x 4 x 3 x 2 x 1 = 120

#4. Print the factorial.
print(f"the factorial of {user_input}is {factorial}")