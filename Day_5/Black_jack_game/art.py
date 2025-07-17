import random
import art
user_card = []
computer_card = []
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))
    return user_card,computer_card

def score_calculator(user,computer):
    user_score = sum(user_card)
    computer_score = sum(computer_card)
    return user_score,computer_score