from random import randint

EASY_LEVEL_TURNS = 10 #global variable, which can be used anywhere
HARD_LEVEL_TURNS = 5


# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficult. Type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Function to check the user's guessed number against actual answer
def check_answer(guess,answer,turns):
    """check answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print("You got it!The answer was {answer}")

def game():
    # Choosing a random number between 1 and 100
    answer = randint(1,100)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    turns = set_difficulty()


    # Repeating the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        # Let the user guess the number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns) #這邊turns區域變數的值又會再次被更新
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return #return 可以用來結束迴圈
        elif guess != answer:
            print("Guess again!")



# Track the number of turns and reduce by 1 if they got it wrong


game()




"""
不好的示範: 在function內去修改global的值

EASY_LEVEL_TURNS = 10 #global variable, which can be used anywhere
HARD_LEVEL_TURNS = 5
# Choosing a random number between 1 and 100
answer = randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
# Make function to set difficulty
def set_difficult():
    level = input("Choose a difficult. Type 'easy' or 'hard'")
    global turns
    if level == "easy":
        turns = EASY_LEVEL_TURNS
    else:
        turns = HARD_LEVEL_TURNS

guess = int(input("Make a guess: "))
turns = 0
set_difficult()
print(f"You have {turns} attempts remaining to guess the number")

"""