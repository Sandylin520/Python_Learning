import random
#from replit import clear
#from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def cal_user_score():
    # user_score = 0
    # for item in user_list:
    #     user_score += item
    # return user_score
    return sum(user_list)

def cal_com_score():
    # com_score = 0
    # for item in com_list:
    #     com_score += item
    # return com_score
    return sum(com_list)

def user_get_card():
    card = deal_card()
    user_list.append(card)

def com_get_card():
    card = deal_card()
    com_list.append(card)

com_list = []
user_list = []

#random picked two cards and save it into the list
for _ in range(2):
    user_list.append(deal_card())

for _ in range(2):
    com_list.append(deal_card())

user_win = False
play_game = True
while play_game:
    #print(cal_user_score())
    user_score = cal_user_score()
    #print(cal_com_score())
    com_score = cal_com_score()
    if sum
    print(f"you get card {user_list}, your score is {user_score}")
    print(f"computer gets card {com_list},computer score is {com_score}")
    #Does the user or computer have a blackjack
    if 11 in user_list or 11 in com_list:
        if 11 in com_list: #com has blackjack, com wins
            user_win = False
            print(f"You lost!, computer gets blackjack")
            break
        else:#user has blackjack, com doesnt
            user_win = True
            print(f"You win!you get blackjack")
            break
    else:
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
        #user_score < 21, ask whether user wnat ot get another card
        will = input("Do you want to get another card? please enter 'y' or 'n' ").lower()
        if will == "y":
            user_get_card()
            continue #verify whether new card is Ace and total our of 21 or not
        else:
            while com_score < 17:
                com_get_card()
                continue #verify whether new card is Ace ,doesnt matter total our of 21 or not


        if com_score > 21:
            user_win = True
            print(f"you win, computer score {com_score} is over 21")
            break
        if user_score > com_score:
            user_win = True
            print(f"you win, {user_score} is higher than {com_score}")
            break
        elif user_score < com_score:
            user_win = False
            print(f"you lost!, {user_score} is lower than {com_score}")
            break
        else:#user score = com_score
            print("draw")
            print(f" User score {user_score} is same as computer score {com_score}")
            break

play_again = input("Do you want to play the game again? Enter 'y' or 'n' ")
if play_again == "n":
    play_game = False
    print("Goodbye")