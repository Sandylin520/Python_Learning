rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#rock:0 paper:1 scissors:2
game_image = [rock,paper,scissors]

print("Let's play rock paper scissors game, 0 for Rock, 1 for Paper, 2 for Scissors :")
user_choice = int(input("What do you choose? "))
if user_choice > 2 or user_choice <0 :
    print("invalid input")
else:
    print("You chose:")
    print(game_image[user_choice])

    cp_choice = random.randint(0,2)#0~2
    print("Computer chooses")
    print(game_image[cp_choice])

    if  user_choice == cp_choice:
        print("you two are even,try again")
    elif (cp_choice == user_choice+2) or (user_choice-cp_choice==1): #win: 0 2; 1 0; 2 1
        print("Congradulatin, you win the computer!")
    else:
        print("Ah! sorry ! You lost !")