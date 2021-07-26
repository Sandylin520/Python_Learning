import random
#from replit import clear
#from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

com_list = []
user_list = []

def cal_user_score():
    user_score = 0
    for item in user_list:
        user_score += item
    return user_score


def cal_com_score():
    com_score = 0
    for item in com_list:
        com_score += item
    return com_score

user_win = False

def user_get_card():
    card = deal_card()
    user_list.append(card)

def com_get_card():
    card = deal_card()
    com_list.append(card)

def check_result():
    if 11 in com_list: #com has blackjack, com wins
        user_win = False
        print("Lose, opponent has Blackjack😱")
    elif 11 in user_list:
        user_win = True
        print("You win! you get Blackjack😃")
    elif user_win == False:
        print("You lose the game😭")
        print(f" Your score is {user_score} is lower {com_score}")
    elif user_win == True:
        print("User Wins😎")
        print(f" Your score is {user_score} is higher than {com_score}")
    else:
        print("Draw 🙃")
        print(f" Your score {user_score} is same as computer score {com_score}")


game_start = True
while game_start:
    user_get_card()
    user_get_card()
    com_get_card()
    com_get_card()

    # testing use
    # user_list.append(10)
    # user_list.append(10)
    # com_list.append(10)
    # com_list.append(5)

    while not user_win:
        #print(cal_user_score())
        user_score = cal_user_score()
        #print(cal_com_score())
        com_score = cal_com_score()

    #Does the user or computer have a blackjack
    check_result()
    # if 11 in user_list or 11 in com_list:
    #     if 11 in com_list: #com has blackjack, com wins
    #         user_win = False
    #         print("Lose, opponent has Blackjack😱")
    #         break
    #     else:#user has blackjack, com doesnt
    #         user_win = True
    #         print("You win! you get Blackjack😃")
    #         break

    #Is user's score over 21
    if user_score > 21:
        # do user have ace, if has ,swap 11 to 1
        if 11 in user_list:
            position = user_list.index(11)
            user_list[position] = 1
            user_score = cal_user_score()
            if user_score > 21:
                user_win = False
                break
        else:
            user_win = False
            break
    will = input("Do you want to get another card? please enter 'y' or 'n' ").lower()
    if will == "y":
        user_get_card()
        continue
    else:
        while com_score < 17:
            com_get_card()
            continue#add this to check whether Ace exists in com_list

    # if com_score > 21:
    #     user_win = True
    #     break

    # if user_score > com_score:
    #     user_win = True
    #     break
    # elif user_score < com_score:
    #     user_win = False
    #     break
    # else:
    #     break

    check_result()
    break


play_game = input("Do you want to play another game, please enter 'y' or 'n'").lower()
if play_game == "n":
    game_start = False
    print("Goodbye!")

"""

影響遊戲結束關鍵>>
point_1)
Ace出現: cp有 , game over (user掛掉); user有, cp沒有, game over (cp掛掉)

point_2)
遊戲點數:
user >21  給它解救機會，ace從11變1，看是否仍>21，是=>game over
user <21  問user是否在抽牌，抽拍就要再看loop一次看抽到啥、是否大於21，不抽才往下

user不抽,讓cp < 17, cp抽牌
CP>21 => game over
CP<21 => 和user 比較


測試:
讓computer 有11 =>game over(cp win)
讓User有11, cp沒有 => game over(user win)
cp,user都有 => game over (cp win)

讓user>21 => game over (com win), user<21 問要不要抽牌，要就要重算score，不要就換檢查cp score
讓com < 17
讓com>21 => game over(user win)

"""