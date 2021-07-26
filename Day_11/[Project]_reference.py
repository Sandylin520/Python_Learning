import random
from replit import clear
from art import logo

card_values = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def deal_cards(player, score):
    #picks random card from list and appends to player's
    card = random.choice(deck)
    player.append(card)
    #changes value of Ace based on player's total
    if card == "A" and score + 11 > 21:
        score = 1
    else:
        score = card_values[card]
    return score

def hit_pass():
    global user_total
    global dealer_total
    ht_ps = input("Hit or pass? type 'h' or 'p': ").lower()
    if ht_ps == "h":
        user_total += deal_cards(user_cards, user_total)
        #deals with user total if user goes over 21
        if user_total > 21:
            print(f"Your final hand is {user_cards} and your final score is {user_total}")
            print(f"The computer's final hand is {dealer_cards} and its final score is {dealer_total}")
            print("You lose!😭")
        else:
            print(f"Your current hand is {user_cards} and your current score is {user_total}")
            hit_pass()
    else:
        #computer will keep drawing cards until score is at least 17
        while dealer_total < 17:
            dealer_total += deal_cards(dealer_cards, dealer_total)
        print(f"Your final hand is {user_cards} and your final score is {user_total}")
        print(f"The computer's final hand is {dealer_cards} and its final score is {dealer_total}")
        if len(dealer_cards) == 2 and dealer_total == 21:
            print("BlackJack! You Lose!😭")
        elif dealer_total > user_total and dealer_total <= 21:
            print("You lose!😭")
        elif user_total == dealer_total:
            print("Draw!🙃")
        else:
            print("You win!😁")

play_blkjck = input("Want to play Black Jack? type 'y' or 'n': ").lower()

while play_blkjck == 'y':
    print(logo)
    user_cards = []
    user_total = 0

    dealer_cards = []
    dealer_total = 0

    #initial two card deal for user and computer
    user_total += deal_cards(user_cards, user_total)
    user_total += deal_cards(user_cards, user_total)

    dealer_total += deal_cards(dealer_cards, dealer_total)
    dealer_total += deal_cards(dealer_cards, dealer_total)

    #deals with initial BlackJack
    if user_total == 21 and dealer_total == 21:
        print(f"Your final hand is {user_cards} and your final score is {user_total}")
        print(f"The computer's final hand is {dealer_cards} and its final score is {dealer_total}")
        print("Draw!🙃")

    elif user_total == 21:
        print(f"Your final hand is {user_cards} and your final score is {user_total}")
        print(f"The computer's final hand is {dealer_cards} and its final score is {dealer_total}")
        print("BlackJack! You win!😁")
    else:
        #prints user's hand and first card in computer's deck
        print(f"Your current hand is {user_cards}, and your score is {user_total}")
        print(f"The first card in the computer's deck is {dealer_cards[0]}")
        hit_pass()

    play_blkjck = input("Want to play Black Jack? type 'y' or 'n': ").lower()
    clear()