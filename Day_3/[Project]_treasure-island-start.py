print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# #way_1
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# direction = input("Choose your direction, right or left ")
# #action = input("Choose you action, swim or wait")
# #colored_door = input("Choose your door color, Blue, Red, Yellow ")

# if direction != "left":
#     print("Fall into a hole, Game over! ")
# else:
#     action = input("Choose you action: swim or wait ")
#     if action != "wait":
#         print("Attacked by trout, Game over! ")
#     else: #遊戲繼續
#         colored_door = input("Choose your door color: Blue or Red or Yellow ")
#         if (colored_door != "Red") and (colored_door != "Yellow") and (colored_door !="Blue"):
#             print("Game over!")
#         else:#遊戲繼續
#             if colored_door == "Red":
#                 print("Burned by fire, Game over!")
#             elif colored_door ==  "Yellow" :
#                 print("You win!")
#             else:  #blue
#                 print("Eaten by beasts, Game over!")

#way_2
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("Choose your direction, right or left ").lower()
#action = input("Choose you action, swim or wait")
#colored_door = input("Choose your door color, Blue, Red, Yellow ")
if direction == "left":
    print("You've come to a lake.There is an island in the middle of the lake.")
    print("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    action = input("Choose you action, swim or wait ")
    if action == "wait":
        print("You have arrived the island unharmed.There is a house with 3 doors.")
        print("One red, one yellow, and one blue, which color do you choose? ")
        colored_door = input("Choose your door color, Blue, Red, Yellow ").lower()
        if colored_door == "red":
            print("Burned by fire. Game over")
        elif colored_door == "yellow":
            print("You win")
        elif colored_door == "blue":
            print("Eaten by beasts,Game over!")
        else:
            print("Game over")
    else:
        print("Attacked by trout, Game Over")
else:
    print("You fell into a hole, Game Over!")