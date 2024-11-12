#Name: CJ Nickson
#Class: 6th Hour
#Assignment: HW13
from itertools import count

#1. Create a list containing 10 integers of your choice.
numbers=[1,2,3,4,5,6,7,8,9,10]
#2. Create two empty variables named evenNumbers and oddNumbers.
evennumbers=[]
oddnumbers=[]
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for number in numbers:
    if number % 2==0:
        evennumbers.append(number)
    else:oddnumbers.append(number)

    count_even = len(evennumbers)
    count_odd = len(oddnumbers)
# Print the total count of even and odd numbers.
print("number of even numbers:",count_even)
print("number of odd numbers:",count_odd)