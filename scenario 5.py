#Name: CJ and Logan
#Class: 6th Hour
#Assignment: Scenario 5

#Scenario 5
#You're all part of a new development team and the big wigs want to see what you are all capable of.
#They want you to develop whatever you want to develop, but there's only one problem:
#the same big wigs only bought enough computers for half of you. Because of this, you will
#all be split into teams of two. One serving as the brain (not using the computer),
#one serving as the hands (using the computer).
import random

#You have until the Scenario is due to brainstorm an idea together, create a flowchart, and then
#turn that flowchart into functioning code. The code itself must have at least: 1 dictionary or list,
#1 loop, 2 if statements (elif and else statements tied to it does not count towards the total),
#1 variable with a user input, and 1 form of an assignment operator. You are free to add whatever else
#you feel is necessary to complete your concept. You will be graded based on how those ideas are
#implemented together.

gamelist =["nba 2k","ncaa 25","hollow knight","elden ring"]
numlist =[2,3,4,5,10,11,12,13,14,15,20,21,23,24,35]
teamlist=[]
i = 0
list = int(input("choose a list:"))
if list == 1:
    x = gamelist[random.randint(0,3)]
    print(x)
    y = gamelist[random.randint(0,3)]
    if y  !=x:
        print(y)
        z = gamelist[random.randint(0,3)]
        if z !=x and z !=y:
            print(z)
            r = gamelist[random.randint(0,3)]
            if r !=x and r !=y and r !=z:
                print(r)
            else:
                print("no")
        else:
            print("no")

    else:
        print("sorry you already played that")


if list == 2:
    for i in range (1,6):
        tempplayer =random.choice(numlist)
        teamlist.append(tempplayer)
        numlist.remove(tempplayer)


    print(teamlist)