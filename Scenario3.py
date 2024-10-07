#name CJ Nickson
#class 6th hour
#assigment scenario3

print("helloworld")

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.\
import random

roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
roll3 = random.randint(1,6)
roll4 = random.randint(1,6)
roll5 = random.randint(1,20)
enemydict = {
    "enemy1" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 19,
        "armor" : 17,
        "Damage" : roll1,
        "attack mod" : 5
    },
    "enemy2" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 18,
        "armor" : 14,
        "Damage" : roll1,
        "attack mod" : 4
    },
    "enemy3" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 17,
        "armor" : 14,
        "Damage" : roll1,
        "attack mod" : 3
    },
    "enemy4" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 16,
        "armor" : 10,
        "Damage" : roll1,
        "attack mod" : 7
    }
}
playerdict = {
    "player1": {
     "name" :"Ethan Downs",
     "damage":roll1,
        "Health": 15,
        "armor": 17,
    "attack mod" : 4
},

    "player2" :{
    "name":"R mason",
    "damage":roll1,
        "Health": 10,
        "armor": 15,
    "attack mod" : 6
},

"player3" :{
    "name":"pj",
    "damage":roll1,
    "Health": 11,
    "armor": 13,
    "attack mod" : 5
},

"player4" :{
    "name":"T weinn",
    "damage":roll1,
    "Health": 12,
    "armor": 12,
    "attack mod" : 4
}
}

d20=roll5
if enemydict["enemy1"]["attack mod"] + d20 > playerdict["player1"]["armor"]:
    print("enemy1 attack hits")
    if playerdict ["player1"]["Heath"] > 0:
        if enemydict["player1"]["attack mod"] + d20 > playerdict["enemy1"]["Health"]:
            print("player1 attacks hits, enemy1 Health is")
            print(playerdict["player1"]["damage"] - enemydict["enemy1"]["Health"])
        elif playerdict["player1"]["attack mod"] + d20 < enemydict ["enemy1"]["Health"]:
            print("player1 attack misses")
    elif enemydict ["enemy1"]["attack mod"] + d20 < playerdict["player1"]["Health"]:
        print("enemy1 attack misses")
elif playerdict["player1"]["attack mod"] + d20 < enemydict ["enemy1"]["armor"]:
    print("player1 attack misses")





#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4




#Party Dictionary Goes Here



#Enemy Dictionary Goes Here



#Combat Code Goes Here