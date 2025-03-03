#name CJ Nickson
#class 6th hour
#assigment HW6

print("helloworld")

#2. Create a variable named num and assign it a number.
num=10
#3. Create a nested if statement follows this structure:

#If num is divisible by 2
#   if num is divisible by 3
#       print the result of num being divided by 2
#       print the result of num being divided by 3
#   else
#       print that it is not divisible by 3
#       print the result of num being divided by 2
#else
#   if num is divisible by 3
#       print that num is not divisible by 2
#       print the result of num being divided by 3
#   else
#       print that neither is divisible by 2 or 3

if num % 2==0:
    if num % 3==0:
        print(num / 2)
        print(num / 3)
    else:
        print("num is not % by 3")
        print(num / 3)
else:
    if num % 3==0:
        print("num is not % by 2")
        print(num / 3)
    else:
        print("not % by 2 or 3")


import random
import time

class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    # Step 4: Function for the warrior to take random damage
    def take_damage(self):
        for _ in range(10):  # Loop 10 times
            damage_taken = random.randint(1, 6)  # Random damage between 1 and 6
            self.health -= damage_taken
            print(f"Warrior takes {damage_taken} damage. New health: {self.health}")
            time.sleep(1)  # Delay of 1 second

    # Step 6: Function for the healer to heal the warrior
    def heal(self, target):
        heal_amount = 30
        target.health += heal_amount
        if target.health > 100:  # Max health check
            target.health = 100
        print(f"Healer heals Warrior for {heal_amount} health. Warrior's new health: {target.health}")

# Step 3: Create the "warrior" character object
warrior = Character(health=100, damage=20, speed=30)
print(f"Warrior's initial health: {warrior.health}")

# Call the take_damage function for the warrior
warrior.take_damage()

# Step 5: Create the "healer" character object
healer = Character(health=60, damage=10, speed=30)

# Step 6: Heal the warrior
healer.heal(warrior)

# Step 7: Print the final health of the warrior
print(f"Warrior's final health: {warrior.health}")

























