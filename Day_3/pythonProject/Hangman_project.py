import random
import Hangamn_art

print(Hangamn_art.pic)
print("Welcome to Hangman Game!!")
words = ["Chandu","Theju","Appaji","Amma","God","Python"]

selected_word =random.choice(words)

boolean = True
life = 6
# word_length = len(selected_word)
blank = []
for i in selected_word:
    blank.append("_")
print(blank)

hangman_count =0
while boolean:
    first = True
    second =True

    store = ""
    print(f"Word to Guess: {blank}" )
    user_input = input("Guess a letter")
    count = -1
    for i in selected_word:
        count += 1
        if user_input == i:
            if user_input in blank:
                print(f"You already guessed {user_input}")
                second = False
                first = False

            while first:
                blank[count] = i
                for printing_word in blank:
                    store += printing_word
                    # print(store)
                print(store)
                print(Hangamn_art.HANGMANPICS[hangman_count])
                print(f"************************{life}/6 LIVES LEFT ********************")
                if "_" not in blank:
                    print("You Guess it right, You Won !!!!!!")
                    boolean = False
                    second = False
                second = False
                break

    while second:
        hangman_count +=1
        life -=1
        print(f"You guessed {user_input}, that's not in the word. You lose a life.")
        print(Hangamn_art.HANGMANPICS[hangman_count])
        print(f"************************{life}/6 LIVES LEFT ********************")
        if life == 0:
            boolean = False
            print("Game Over You Loose")
        second = False



