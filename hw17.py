#Name: CJ Nickson
#Class: 6th Hour
#Assignment: HW17


#1. Import the "random" library and create a def function that prints "Hello World!"
import random

from hw15 import hello_world


def print_hello_world():
  print("Hello World!")

print_hello_world()
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
for i in range (100):
    if random.choice(['heads','tails'])=='heads':
        heads += 1
        tails += 1
    print("heads:")
    print("tails")
#4. Call the "Hello world" and "Coin Flip" functions here
print("helloworld"("flip coin"))
#5. Print the final result of heads and tails here