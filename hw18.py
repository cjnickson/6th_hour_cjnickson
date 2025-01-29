#Name:CJ Nickson
#Class: 6th Hour
#Assignment: HW18
from itertools import filterfalse

from hw15 import hello_world

#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanbag = ["red","blue","green","yellow","purple"]
print(beanbag)
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.

import random
def pull_random_bean(beanbag):
    if beanbag:
        random_bean=random.choice(beanbag)
        print(f"pulled bean:{random_bean}")
        beanbag.remove(random_bean)
    else:
        print("no beans left to pull")
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
import random
def pull_random_bean(beanbag):
    if beanbag:
        random_bean=random.choice(beanbag)
        print(f"pulled bean:{random_bean}")
        beanbag.remove(random_bean)
    else:
        print("no beans left to pull")
        return False
    return True
def ask_to_pull_another(beanbag):
    while beanbag:
        if not pull_random_bean(beanbag):
            break
            answer=input("do you want to pull another bean?(yes/no):").strip().lower()
            if answer!='yes':
                break
                print("no more beans will be pulled.")
#5. Call the #3 function at the bottom.
hello_world()