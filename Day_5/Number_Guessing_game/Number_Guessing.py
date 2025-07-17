import random
import art


print(art.logo)
print("Welcome to number Guessing Game!\nI'm Thinking of a number between 1 and 100 ")
computer_random_number = random.randint(1,100)
level = input("choose a difficulty. Type 'easy' or 'hard': ").lower()

def guessing():
    game = True
    if level == "easy":
        attempt = 10
    elif level  == "hard":
        attempt = 5
    else:
        print("Wrong input")
        return
    while game:
        print(f"You have {attempt} attempts remaining to guess the number.")
        if attempt == 0:
            print("You've run Out of attempt sorry play again")
            game = False
            break
        guess = int(input("Make a Guess : "))
        if guess > computer_random_number:
            print("Too High\nGuess Again")
            attempt -=1
            # break
        elif guess < computer_random_number:
            print("Too Low\n Guess Again")
            attempt -=1
            # break
        elif guess == computer_random_number:
            print(f"You got the right answer {computer_random_number}")
            game = False
        else:
            print("Wrong input number")


guessing()