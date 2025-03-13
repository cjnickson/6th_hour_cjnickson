#Name: CJ Nickson
#Class: 6th Hour
#Assignment: HW23

#1. Import the random and time libraries

import random
import time

class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed


#3. Make a "warrior" character object with 100 health, 20 damage, and 30 speed. Print the character's initial health below.

def take_damage(self):
          for _ in range(10):  # Loop 10 times
            damage_taken = random.randint(1, 6)  # Random damage between 1 and 6
            self.health -= damage_taken
            print(f"Warrior takes {damage_taken} damage. New health: {self.health}")
            time.sleep(1)
#4. Make a def function within the class that loops 10 times. Within this function,
#make the following loop 10 times: the character takes a random amount of damage from 1 to 6,
#the new health is printed, a time.sleep delay of one second is done. Call the function to the warrior.
def heal(self, target):
        heal_amount = 30
        target.health += heal_amount
        if target.health > 100:  # Max health check
            target.health = 100
        print(f"Healer heals Warrior for {heal_amount} health. Warrior's new health: {target.health}")
#5. Make a "healer" character object with 60 health, 10 damage, and 30 speed.
warrior = Character(health=100, damage=20, speed=30)
print(f"Warrior's initial health: {warrior.health}")
#6. Make a def function within the class that heals the warrior for 30 health. Create an if statement
#that sets the warrior's health to its max (100) if the healing would bring the warrior's health above that.
#Call the function to the healer.

#warrior.take_damage()

healer = Character(health=60, damage=10, speed=30)
#healer.heal(warrior)
#7. Print the warrior's final health at the very bottom.
print(f"Warrior's final health: {warrior.health}")
