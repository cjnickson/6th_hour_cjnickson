#name CJ Nickson
#class 6th hour
#assigment HW4
print("helloworld")

carDict = {
    "brand" : "dodge",
    "model":"charger",
"year" : [2021,2022, 2023]
}

print(carDict)
print(carDict["model"])

print(carDict["year"][2])

carDict["color"] = "black"
print(carDict)

carDict.update({"wheels":4})
print(carDict)

carDictValues = carDict.values()
print(carDictValues)

carDict.pop("wheels")
print(carDict)

fifthHour = {
 "student1": {
   "name" : "CJ",
    "grade" : 12,
 "sports" : True,
},
"student2":{
    "name" : "tate",
    "grade" : 12,
    "sports" : True,
},
"student3":{
    "name" : "ethan",
    "grade" : 12,
    "sports" : True,
},
}

print(fifthHour["student1"]["name"],fifthHour["student2"]["name"],fifthHour["student3"]["name"])