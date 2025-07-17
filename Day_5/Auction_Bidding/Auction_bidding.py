import logo
dictonary = {}

print(logo.logo)
game_loop = True

def highest_bidder(dict):
    winner = ""
    highest_bid = 0
    for key in dict:
        bid_amount = dict[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"The Winner is {winner} with a bid of ${highest_bid}")

while game_loop:
    name = input("What is Your name?:  ")

    bid_price = int(input("What is your bid?: $  "))

    dictonary[name] = bid_price

    other_bidders = input("are there any other bidders? Type 'yes' or 'no'. ").lower()

    if other_bidders == "no":
        game_loop = False
        highest_bidder(dictonary)
    elif other_bidders == "yes":
        print("\n"*50)
    else:
        print("Wrong input")
        game_loop = False

