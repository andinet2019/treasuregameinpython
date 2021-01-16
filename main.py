import random

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# list
#

# logical operators in python
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
resp1 = input("You are at the cross road .Where do you want to go? Type 'left' or 'right  ")
if resp1 == "left":
    resp2 = input(
        "You come to a lake .There is an island in the middle of the lake.Type 'wait to wait for a boat .Type 'swim' to swim across ")
    if resp2 == "wait":
        resp3 = input("You arrived at the island unharmed.There is a house with 3 doors.One red,one yellow and one blue ,Which color do you choose?'blue' or 'yeloow?'Type ' ")
        if resp3 == "blue":
            print("You are eaten by beasts.Game is over")
        elif resp3 == "yellow":
            print("You win")
        elif resp3 == "red":
            print("Burned by fire.Game over")
        else:
            print("Game Over")


elif resp1 == "right":
        print("Fall into a hole.Game is over")
