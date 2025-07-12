import random

import rock_paper_scissors_art
computer = random.randint(0,2)
user_input = int(input("What do You choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))

if user_input == 0:
    print(rock_paper_scissors_art.rock)
elif user_input == 1:
    print(rock_paper_scissors_art.paper)
elif user_input == 2:
    print(rock_paper_scissors_art.scissors)
else:
    print("Wrong Input")
print("Computer Chose:")
if computer == 0:
    print(rock_paper_scissors_art.rock)
elif computer == 1:
    print(rock_paper_scissors_art.paper)
else:
    print(rock_paper_scissors_art.scissors)

if user_input == computer:
    print("It's Draw")
elif user_input == 0 and computer == 1 or user_input == 1 and computer == 2 or user_input == 2 and computer == 0:
    print("Computer wins")
else:
    print("You won")
