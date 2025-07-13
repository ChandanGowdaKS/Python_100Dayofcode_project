import random

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

numbers = [1,2,3,4,5,6,7,8,9,0]

Symbols = ["!","@","#","$","*","(",")"]

print("Welcome to the Password Generator!")

# # input from user
user_letter = int(input("How many letters would ypu like in your password?\n"))
user_symbol = int(input("How many symbols would you like?\n"))
user_number = int(input("How many numbers would you like?\n"))
final_list = []

final_list.extend(random.choices(letters,k=user_letter))
final_list.extend(random.choices(Symbols,k=user_symbol))
final_list.extend(random.choices(numbers,k=user_number))

print(random.sample(final_list,k=len(final_list)))


