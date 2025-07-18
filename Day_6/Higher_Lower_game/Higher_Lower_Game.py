import art
import game_data
import random

score = 0
# random coice generator function
def generator():
    return random.choice(game_data.data)

# Comparision for A data
def comparision_A():
    print(f"Compare A:{generated["name"]},{generated["description"]},{generated["country"]}")
    a_data = generated
    return a_data
# Comparision for B data
def comparision_B():
    print(f"Compare B:{generated["name"]},{generated["description"]},{generated["country"]}")
    b_data = generated
    return b_data
# comparision function for both data
def both_comparision(a_data,b_data,game):
    global score
    if a_data["follower_count"] > b_data["follower_count"] and user_input == "a":
        # global score
        score +=1
        print(f"You're right!! Current Score {score}")
    elif a_data["follower_count"] < b_data["follower_count"] and user_input == "b":
        # global score
        score += 1
        print(f"You're right!! Current Score {score}")
    elif a_data["follower_count"] == b_data["follower_count"]:
        print("It's Draw")
    else:
        print(f"Sorry that's wrong. Final Score is {score}")
        game = False
    return game


Game = True
while Game:
    print(art.logo)
    generated = generator()
    final_a_data = comparision_A()
    print(art.vs)
    generated = generator()
    final_b_data = comparision_B()
    user_input = input("Type 'A' or 'B'").lower()
    Game = both_comparision(final_a_data,final_b_data,Game)