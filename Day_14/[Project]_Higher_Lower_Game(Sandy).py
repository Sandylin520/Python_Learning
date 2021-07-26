
import random
from art import logo,vs
from game_data import data
import os
def clear(): os.system('cls') #on Windows System


def format_data(item):
    """Take the account data and return the printable format"""
    item_name = item['name']
    item_description = item['description']
    item_country = item['country']
    return (f"{item_name}, a {item_description}, from {item_country}")

def has_more_followers(A,B):
    """Return the one (A,B) has most followers"""
    if A['follower_count']> B['follower_count']:
        return "a"
    else:
        return "b"

def check_the_answer(user_guess,answer):
    """Function checks whether user input is correct, if correct returns True, otherwise returns False"""
    if user_guess == answer:
        print("Congradulation! You win one point!")
        return True
    else:
        print("Sorry,that's wrong. Computer wins!")
        return False

#check end of game or not
def check_end_of_game(questions,game_ended,user_score,cp_score):
    """if question is equal to 0, game ended"""
    if questions == 0:
        game_ended = True
        if cp_score > user_score:
            print(f"You win! Your score is {user_score}")
        elif cp_score < user_score:
            print(f"You Lost! Your score is {user_score}")
        else:
            print("Draw!")
    return game_ended





print(logo)
print("Welcome to the game!You get 10 questions waiting ahead of you")
print("If your answer is correct, you win a point. Otherwise, computer wins instead")
print("By the end of the game, the one who wins most point is the winner.")
print()

def game():
    user_score = 0
    cp_score = 0
    questions = 10
    game_ended = False
    number = 0
    while not game_ended:
        number += 1
        print(f"Question: {number}")
        print(f"Your current score is {user_score}, computer score is {cp_score}")
        #Generate data
        A = random.choice(data)
        if number != 1:
            A = C
        B = random.choice(data)
        if B == A:
            B = random.choice(data)
        C = B

        #print data
        print(f"Compare A:  {format_data(A)}")
        print(vs)
        print(f"Against B:  {format_data(B)}")

        #Ask user for input
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        #define the correct answer and save it
        answer = has_more_followers(A,B)
        #check use's answer and save and return True or False
        right_guess = check_the_answer(user_guess,answer)
        questions -=1

        #track user and cp score
        if right_guess == True:
            user_score += 1
            print(f"Your current score is {user_score}")
        else:
            cp_score += 1
            print(f"Your current score is {user_score}")
        #clear the screen()
        clear()
        #add_score(right_guess,user_score,cp_score)
        game_ended = check_end_of_game(questions,game_ended,user_score,cp_score)

game()