#name CJ Nickson
#class 6th hour
#assigment HW6
from operator import truediv

print("helloworld")

wifi=True
login=False
admin=True

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
adminlogin=55
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".

if wifi==True:
    if login==True:
        if admin==True:
            adminlogin +=1
            print("welcome")
        else:
            print("no admin")
    else:
        print("no login info")
else:
    print("no wifi")