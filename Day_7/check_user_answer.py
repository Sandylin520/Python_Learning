import random

word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for letter in chosen_word:  #for letter in range(len(chosen_word)):
    display += "_"
print(display)

while "_" in display:
    #讓使用者輸入字母
    guess = input("Guess a letter: ").lower()
    #checked guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter:{letter}\n Guessed letter:{guess}")
        if letter == guess:
            display[position] = letter
            print(display)


"""
目的: 將選中的單詞改成"_"加密:
可透過字串相加，用 += ,將"_" 加入空字串("")
也可用append方法，將元素"_"加到列表中

display = []
for letter in chosen_word:
    display += "_"
print(display)

display = []
for i in range(len(chosen_word)):
    display.append('_')
print(display)




目的:[Way_2]當字母被猜中時，將"_"改由猜中字母取代
while "_" in display:
    guess = input("Guess a letter: ").lower()

    index = -1 #index值是用來幫助將猜到的字母取代"_"
    for item in chosen_word:
        index += 1
        #確認輸入的字母是否符合chosen_word的任一個字母
        if guess == item:
            #若符合，猜的字母取代 "_"
            display[index] = guess
            print(display)
print(display)

"""