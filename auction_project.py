# Secret Auction Project

from auction_art import logo
print(logo)
print("Welcome to the secret auction!")
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder 
    
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $ "))
    bids[name] = price
    people  = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if people == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif people == "yes":
        print("\n" * 20)
