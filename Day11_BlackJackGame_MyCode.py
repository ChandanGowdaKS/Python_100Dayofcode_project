import random
# from distutils.command.build_scripts import first_line_re
# from importlib import invalidate_caches

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def continue_game(game,name):
    computer_list = []
    player_list = []
    comp_score = 0
    player_score = 0
    first = True
    while first:
        if game == "y":
            for i in range(2):
                computer = random.choice(cards)
                computer_list.append(computer)
                comp_score += computer
                player = random.choice(cards)
                player_list.append(player)
                player_score += player
            computer_score_matching = True
            while computer_score_matching :
                if comp_score < 17:
                    computer = random.choice(cards)
                    computer_list.append(computer)
                    comp_score += computer
                else:
                    computer_score_matching = False

            print("Computer's First Card is :",computer_list[0])
            print(f"{player_list} {name} Your Score is {player_score}\n")
            if player_score >= 21:
                if 11 in player_list:
                    player_score -=10
                first = False
                second = False
            second = True
            while second:
                next_card = input(f"{name} Do you Want One More Card Type 'y' or 'n' \n")
                if next_card == "y":
                    player = random.choice(cards)
                    if player == 11:
                        if player_score + player >= 21:

                            player = 1
                    player_list.append(player)
                    player_score += player
                    print("Computer's First Card is :",computer_list[0])
                    print(f"{player_list} {name} Your Score is {player_score}\n")
                    if player_score >= 21:
                        print(f"You Loose {name} Your Score is Exceeded by 21 ")
                        first = False
                        second = False
                        call()
                elif next_card == "n":
                    second = False
                    first = False
                    # print(f"Computer's Score is {comp_score}" )
                    # print(f"{player_list} {name} Your Score is {player_score}\n")
                    if player_score <= 21:
                        if comp_score <= 21:
                            if player_score > comp_score:
                                print(f"{name} You won,You's Card are {player_list} Your Score is {player_score}")
                                print(f"Computer's Card are {computer_list} And it's Score is {comp_score}")
                            elif player_score == comp_score:
                                print(f"{name} It's A Draw, Your Score is {player_score}")
                                print(f"Computer's Card are {computer_list} And it's Score is {comp_score}")
                            else:
                                print(f"{name} You loose, You's Card are {player_list} Your Score is {player_score}")
                                print(f"Computer's Card are {computer_list} And it's Score is {comp_score}")
                        else:
                            print(f"Computer Loose, Computer's Card are {computer_list} And it's Score is {comp_score}")
                            print(f"{name} You won,You's Card are {player_list} Your Score is {player_score}")
                    else:
                        print(f"{name}Your Score is Exceeded by 21, You Loose, Your Score is  {player_score}")

                    call()


                else:
                    print("Invalid input")

        elif game == "n":
            print(f"Thank you {name} See You Soon ")
            first = False
        else:
            print("Invalid Input")
            game = input(f'''Hi, Do You want to play Blackjack Game,
if Yes Type "y", If No Type "n"\n''').lower()


def call():
    play = input(f'''Hi, Do You want to play Blackjack Game,
if Yes Type "y", If No Type "n"\n''').lower()
    print("""
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """)
    name_input = input("Enter Your Name :\n").title()



    continue_game(game=play,name=name_input)


call()