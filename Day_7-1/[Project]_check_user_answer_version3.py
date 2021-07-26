import os
def clear(): os.system('cls') #on Windows System

import random
#from hangman_words import word_list
#from hangman_art import logo,stages

logo = ('''

 █████   █████
░░███   ░░███
 ░███    ░███   ██████   ████████    ███████ █████████████    ██████   ████████
 ░███████████  ░░░░░███ ░░███░░███  ███░░███░░███░░███░░███  ░░░░░███ ░░███░░███
 ░███░░░░░███   ███████  ░███ ░███ ░███ ░███ ░███ ░███ ░███   ███████  ░███ ░███
 ░███    ░███  ███░░███  ░███ ░███ ░███ ░███ ░███ ░███ ░███  ███░░███  ░███ ░███
 █████   █████░░████████ ████ █████░░███████ █████░███ █████░░████████ ████ █████
░░░░░   ░░░░░  ░░░░░░░░ ░░░░ ░░░░░  ░░░░░███░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░ ░░░░░
                                    ███ ░███
                                   ░░██████
                                    ░░░░░░
''')


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


print(logo)
#Testing code
print(f"The chose word is {chosen_word}")

#Create blanks
display = []
for letter in chosen_word:  #for letter in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False

lives = 6
while not end_of_game:

    guess = input("Guess a letter: ").lower()

    clear()
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've have already guessed {guess}")

    #checked guessd letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # 取代print(display) #印出陣列
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")#將陣列元素變成字串

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the chose word,you lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    from hangman_art import stages
    print(stages[lives])


    if "_" not in display:
        end_of_game = True
        print("You win")

"""
Join all the elements in the list and turn it into a String.
說明: print(f"{' '.join(display)}")
a = ' '.join(display)
print(f"{a}")

"""