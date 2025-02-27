#Name: CJ nickson
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).

sports = {
    "sport1": {
        "name": "Basketball",
        "players": 5,
        "uses_ball": True
    },
    "sport2": {
        "name": "Soccer",
        "players": 11,
        "uses_ball": True
    },
    "sport3": {
        "name": "Volleyball",
        "players": 6,
        "uses_ball": True
    }
}

#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum

def sum_players(sport1, sport2, sport3):
    total_players = sport1["players"] + sport2["players"] + sport3["players"]
    print("Total number of players in all three sports:", total_players)

#3. Call the function with arguments here

sum_players(sports["sport1"], sports["sport2"], sports["sport3"])
