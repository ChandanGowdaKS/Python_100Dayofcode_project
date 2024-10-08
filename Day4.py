#                                       Stone Paper Scissors Game
from encodings.ascii import StreamConverter


stone =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper =("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissors =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random
image = [stone,paper,scissors]

name = input("Hi Welcome To Stone Paper Scissors Game,\n"
             "Please Type Your Name to Play The Game\n ")
print(f"Welcme {name} Let's Play a Game\n"
      f"Press 0 For Stone\n"
      f"Press 1 For paper\n"
      f"Press 2 For Scissors\n")
score = 0
# print(f"Your score is {score})

while True:
    user_input = int(input("input your choice"))
    # print("\n")
    print(f"Your input is {user_input}")


    print(image[user_input])

    pc_input = random.randint(0,2)
    print(f"PC input is {pc_input}")
    print(image[pc_input])

    if user_input == pc_input:
        print("Its Draw")

    # if user_input == 0 and pc_input == 0:
    #     print(f"Both of You Chosen Rock, So It's Draw ")
    # elif user_input == 1 and pc_input == 1:
    #     print(f"Both of You Chosen paper, So It's Draw ")
    # elif user_input == 2 and pc_input == 2:
    #     print(f"Both of You Chosen scissors, So It's Draw ")

    elif user_input == 0 and pc_input == 2:
        score += 1
        print(f"You Won You Got 1 point, Your Final Score is {score} ")
    elif user_input == 1 and pc_input == 0:
        score += 1
        print(f"You Won You Got 1 point, Your Final Score is {score} ")
    elif user_input == 2 and pc_input == 1:
        score += 1
        print(f"You Won You Got 1 point, Your Final Score is {score} ")

    elif user_input == 0 and pc_input == 1:
        score -= 1
        print(f"You lose, -1 point, Your Final Score is {score} ")
    elif user_input == 1 and pc_input == 2:
        score -= 1
        print(f"You lose, -1 point, Your Final Score is {score} ")
    elif user_input == 2 and pc_input == 0:
        score -= 1
        print(f"You lose, -1 point, Your Final Score is {score} ")
    else:
        print("Please enter Valid Input")


