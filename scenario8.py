#Name: Cj Nickson
#Class: 6th Hour
#Assignment: Scenario8
import random

from Scenario3 import playerdict


#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)


class Character:
    def __init__(self, health, damage, AC, attack_modifier):
        self.health = health
        self.damage = damage
        self.AC = AC
        self.attack_modifier = attack_modifier


enemy1 = Character (19,random.randint (1,6), 17 , 5)
enemy2 = Character (18,random.randint (1,6), 14 , 4)
enemy3 = Character (17,random.randint (1,6), 14 , 3)
enemy4 = Character (16,random.randint (1,6), 10 , 7)

Player1 = Character (15,random.randint(1,6),17,4)
Player2 = Character (10,random.randint(1,6),15,6)
Player3 = Character (11,random.randint(1,6),13,5)
Player4 = Character (12,random.randint(1,6),12,4)







d20=random.randint (1,20)
if enemy1.attack_modifier + d20 > playerdict["player1"]["armor"]:
    print("enemy1 attack hits")
    if playerdict ["player1"]["Heath"] > 0:
        if Player1.attack_modifier + d20 > playerdict["enemy1"]["Health"]:
            print("player1 attacks hits, enemy1 Health is")
            print(playerdict["player1"]["damage"] -enemy1.health)
        elif playerdict["player1"]["attack mod"] + d20 < enemy1.health:
            print("player1 attack misses")
    elif enemy1.attack_modifier + d20 < playerdict["player1"]["Health"]:
        print("enemy1 attack misses")
elif playerdict["player1"]["attack mod"] + d20 <enemy1.attack_modifier:
    print("player1 attack misses")