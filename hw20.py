#Name: CJ Nickson
#Class: 6th Hour
#Assignment: HW20


#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except NameError:
    print("Hello World!")

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num = float(input("enter a number:"))
    result = 100/num
except ZeroDivisionError:
    print("Exception:Divsion by Zero")
except ValueError:
    print("Exception: Invalid input")

#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    num = int(input("enter an integer:"))
    print(num)
except ValueError:
    print("Excepyion: Not an integer")
#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
i=5
while i >=0:
 print(i)
 i -=1
if i <0:
    raise Exception("counter below zero")