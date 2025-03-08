import art
import os

print(art.logo)
print("Welcome to the secret auction program.")

auction_entries = {}

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def new_entries():
    new_name = input("What is your name?: ")
    new_bid = input("What's your bid?: ")
    auction_entries[new_name] = new_bid

def highest_bid_cal():
    highest_bid = 0
    winner = ""
    for bidder in auction_entries:
        new_bid = int(auction_entries[bidder])
        if new_bid > highest_bid :
            highest_bid = new_bid
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")
            
new_entries()

permission = True
while permission:
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other == "yes":
        clear_terminal()
        new_entries()
    elif other == "no":
        permission = False
        highest_bid_cal()
    else:
        print("Invalid Input")

