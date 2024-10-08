# from Day4 import guess
# from Day4 import guess
# import random
#
# word_list = ["aardvark", "baboon", "camel"]
#
# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
#
# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#
# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
# #  is, "Wrong" if it's not.
#
#
# chosen_word = random.choice(word_list)
# print(chosen_word)
#
# guess = input("Hi  guess the letter ").lower()
# print(guess)
#
#
# # while guess != chosen_word:
#
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")


import random
from Day_7_hangman_word import word_list
from Day7_hanganman_art import stages, logo
# word_list = ["chandu", "theju", "ambi"]

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

print(f"You have Total {lives} lives")


placeholder = ""
# word_length = len(chosen_word)
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

correct_letter = []

game = True
while game:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letter:
        print("You Already Guessed this letter")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter

        else:
            display += "_"
    if guess not in chosen_word:
        lives -= 1
        print(f"Your Guessed letter  {guess} is Not in Word list, Try Again")
        print(f"******************{lives} lives left*********************")
        print(stages[lives])
    if lives == 0:
        print("Game Over")
        break
    print(display)

    if "_" not in display:
        game = False
        print("Wow You won")

