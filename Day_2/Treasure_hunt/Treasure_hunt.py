import art_logo
print(art_logo)
print("Welcome to Treasure Hunt!\nYour Mission is to find the Treasure.")
print("You're at a cross Road. Where do you want to go?")
user_input = input('\tType "left" or "right" \n')

if (user_input.lower() == "left"):
    user_input = input("Your in the middle of the lake.\n Type 'Swim' to swim across or Type 'wait' to wait for boat\n")
    if user_input.lower() == "wait":
        user_input = input("Great you're just one step to hunt treasure\n Now there are three boat to select sselect any one Red, yellow, Blue")
        if user_input.lower() == "yellow":
            print("Hurry Finally you Hunted Treasure!!!!")
        elif user_input.lower() == "blue":
            print("Eaten by Whale! , Game over")
        elif user_input.lower() == "red":
            print("Sorry You Jumped to wrong Boat!, You lost")
        else:
            print("Wrong input You Loose!")
    else:
        print("Attacked by Shark! You Loose")
else:
    print("You Fell into a hole you Loose!!")
