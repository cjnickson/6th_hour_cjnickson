#name CJ Nickson
#class 6th hour
#assigment scenario 2
print("helloworld")


partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
    }
}
soonersdict = {
    "player1": {
     "name" :"Ethan Downs",
     "damage":40,
        "Health": 10,
        "AC": 14,
},

    "player2" :{
    "name":"R mason",
    "damage":32,
        "Health": 10,
        "AC": 14,
},

"player3" :{
    "name":"pj",
    "damage":34,
    "Health": 10,
    "AC": 14,
},

"player4" :{
    "name":"T weinn",
    "damage":44,
    "Health": 10,
    "AC": 14,
},

"player5": {
    "name":"danny",
    "damage":16,
    "Health": 10,
    "AC": 14,
}
}
y=partyDictionary["Gale"]["Damage"]
x=soonersdict["player5"]["Health"]
z=y-x
print(z)

