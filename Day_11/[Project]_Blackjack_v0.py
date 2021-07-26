
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
cp_cards = []


#calculate either user or cp card value
def calculate_card(card):
    card_score = sum(card)
    return card_score

def check_blackjack

#pick two cards for cp and user
for _ in range(2):
    #card = deal_card()
    user_cards.append(deal_card())
    cp_cards.append(deal_card())

game_over = False
while not game_over:
    user_score = calculate_card(user_cards)
    com_score = calculate_card(cp_cards)



