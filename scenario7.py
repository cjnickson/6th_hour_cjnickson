#Name:
#Class: 6th Hour
#Assignment: Scenario 7
from scenario6 import characterlist

#Import all of Scenario 6 here

listAverage = 0

def final_average():
    global listAverage
    listAverage = sum(characterlist)/len(characterlist)
    return listAverage

final_average()

print(listAverage)