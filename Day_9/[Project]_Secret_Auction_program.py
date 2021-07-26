print ('''

                     ___________
                     \         /
                      )_______(
                      |"""""""|_.-._,.---------.,_.-._
                      |       | | |               | | ''-.
                      |       |_| |_             _| |_..-'
                      |_______| '-' `'---------'` '-'
                      )"""""""(
                     /_________\
                     `'-------'`
                   .-------------.
                  /_______________\


                  \n\tWELCOME TO THE AUCTION\t\n
''')

import os
def clear(): os.system('cls') #on Windows System


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    #bidding_record ={"Sandy":123, "James":456}
    for bidder in bidding_record:
        #bid_amount = key's value
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


#create dictionaries to store name and bid price
bids = {}
more_bidders = True
while more_bidders:
    name = input("What is your name? ") #key
    price = int(input("What's your bid?: $")) #value
    #assign price to corresponding key's value
    bids[name] = price
    any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'")
    if any_other_bidders == "no":
        more_bidders = False
        clear()
        find_highest_bid(bidding_record=bids)
    else:
        clear()




