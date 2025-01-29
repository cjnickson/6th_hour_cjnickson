#Name:
#Class: 6th Hour
#Assignment: HW19

#1. Import all the functions from the HW15 file.
def hello_world():
 print("hello world!")

hello_world()
def calculate_average(z,y,x):
    a =z+y+x
    print(a/3)
calculate_average(3,5,6)

def animal_list (*animal):
    print("the 3rd animals name is", animal[1])
    animal_list("dog","cat","fish","parrot","monkey")
def numb_loop():
    for i in range (1,13):
        print(i)
        numb_loop()

numb_loop()
animal_list("dog", "cat", "fish", "parrot", "monkey")
calculate_average(3,5,6)
hello_world()
#2. Call the functions here and run HW19.

#3. Delete all calls from HW15 and run HW19 again.