import random

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

#from hangman_words import word_list
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f"The chose word is {chosen_word}")

#Create blanks
display = []
for letter in chosen_word:  #for letter in range(len(chosen_word)):
    display += "_"
print(display)


life = 6
while "_" in display and life>0:
    #Let user enter letter
    guess = input("Guess a letter: ").lower()
    #checked guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)

    if guess not in chosen_word:
        life -= 1 #從陣列最後一項 index 6 開始往前倒數
        print(stages[life])
        if life == 0:
            print("you lost")
            print(f"' '.join(display)")

    if "_" not in display:
        print("you win!")


"""
Way[2]-不一樣的地方: 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值

life = 6
while "_" in display and life>0:
    #讓使用者輸入字母
    guess = input("Guess a letter: ").lower()

    #通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
    if guess in chosen_word: #guess的字母符合chosen_word字串中的任一字母
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display[i] = guess
                print(display)
    else:
        life -= 1
        print(stages[life])#從陣列最後一項開始往前倒數
        if life == 0:
            print("you lost")

    if "_" not in display:
        print("you win!")

"""

