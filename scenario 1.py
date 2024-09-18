#name CJ Nickson
#class 6th hour
#assigment scenario 1
print("helloworld")


sooners = {
    "player1": {
     "name" :"Ethan Downs",
     "damage":(40),
},

    "player2" :{
    "name":"R mason",
    "damage":(32),
},

"player3" :{
    "name":"pj",
    "damage":(34),
},

"player4" :{
    "name":"T weinn",
    "damage":(44),
},

"player5": {
    "name":"danny",
    "damage":(16),
}
}
print(sooners)

sooners["player1"]["damage"]=int(input("enter new damage"))
sooners["player2"]["damage"]=int(input("enter new damage"))
sooners["player3"]["damage"]=int(input("enter new damage"))
sooners["player4"]["damage"]=int(input("enter new damage"))
sooners["player5"]["damage"]=int(input("enter new damage"))

print(sooners)