from Day9 import logo
print(logo)

bidders_list = {}

name = input("Please Enter Your Name :\n")
bid = int(input("Please Enter The Bid Amount :\n"))

bidders_list[name] = bid

# print(bidders_list)
highest = 0
winner_name =""
loop = True

while loop:
    next_bidders = input("Is There any Other User Who want to bid ? Type 'yes' or 'no'\n").lower()
    if next_bidders == "yes":
        print("\n" *100)
        name = input("Please Enter Your Name :\n")
        bid = int(input("Please Enter The Bid Amount :\n"))

        bidders_list[name] = bid
        # print(bidders_list)
    elif next_bidders == "no":
        for nam in bidders_list:

            for high in bidders_list.values():
                if high > highest:
                    highest = high
                    winner_name = nam
        loop = False
        print(f"Thank You\nThe winner is {nam} & Highest bid amount is {highest}")



    else:
        print("Please Enter Vaild Input")
