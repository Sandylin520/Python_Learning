
from random import randint
logo = """
 _____                      _   _                 _
|  __ \                    | \ | |               | |
| |  \/_   _  ___ ___ ___  |  \| |_   _ _ __ ___ | |__   ___ _ __
| | __| | | |/ _ | __/ __| | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __|__ \__ \ | |\  | |_| | | | | | | |_) |  __/ |
 \____/\__,_|\___|___/___/ \_| \_/\__,_|_| |_| |_|_.__/ \___|_|

"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")


def enviroment_setup(entered_challenge_level):
    if entered_challenge_level == "easy":
        return 10
    if entered_challenge_level == "hard":
        return 5

def check_the_number_size(guessed_number,number,attempt,game_ended):
        if guessed_number > number:
            print("Too high. Please guess again")
            print(f"You have {attempt} attempts left ")
            return game_ended #如果沒寫return 迴圈再次進入會是game_ended= None
        elif guessed_number < number:
            print("Too low. Please guess again")
            print(f"You have {attempt} attempts left ")
            return game_ended
        else:#guessed_number == number:
            print("Congradulation! You guess right number!")
            print(f"The number is {number}")
            return not game_ended


#user choses a difficulty
challenge_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#Computer defines number of attempts based on user chosen difficulty
attempt = (enviroment_setup(challenge_level))
print(f"You have {attempt} attempts remaining to guess the number")
#Computer choses a number from 1-100
number = randint(1,100)#include 1 & 100

def game(attempt):
    game_ended = False
    while not game_ended:
        #ask user to guess number
        #guess_number = user_guess_number()
        if attempt == 0:
            game_ended = True
            print(f"You have run out of you chance")
        else:
            #add warning to the user if it's the last chance
            if attempt == 1:
                print("Be careful, this is you last chance to guess")
            guessed_number = int(input("Make a guess: "))
            attempt -=1
            game_ended = check_the_number_size(guessed_number,number,attempt,game_ended)

    print(f"The correct number is {number}")



game(attempt)

