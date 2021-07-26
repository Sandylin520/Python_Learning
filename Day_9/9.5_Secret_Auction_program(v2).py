
# import only system from os
from os import system, name

bidder_info = {}
stop_auction = False

while not stop_auction:
    bidder_name = input("What is your name? ").lower()
    bid = int(input("What is your bid? $"))

    bidder_info[bidder_name] = bid
    clear()

    repeat = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()

    if repeat == "no":
        stop_auction = True
    elif repeat == "yes":
        stop_auction = False
    else:
        print("Invalid input.")
        break

auction_winner = max(bidder_info, key=bidder_info.get)

print(f"The winner is {auction_winner} with a bid of ${bidder_info[auction_winner]}.")