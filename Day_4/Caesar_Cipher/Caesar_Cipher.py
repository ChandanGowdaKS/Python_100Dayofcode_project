# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
from base64 import decode

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

# Todo - 4 Create a function called decrypt() that takes original_text and shift_amount as 2 inputs.

# Todo - 5 Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by
#     the shift_amount and print the decrypted text.
# Todo - 6 Combine the encrypt() and decrypt() functions into a single function called caesar().
#   Use the value of the user chosen direction variable to determine which functionality to use.
#   call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift.

import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
boolean = True

def caesar(direction,text,shift):
    def encrypt(text,shift):
        encode =""
        for char in text:
            if char in alphabet:
                char_index = alphabet.index(char)
                char_index +=shift
                if char_index > 25:
                    char_index -= 26
                encode += alphabet[char_index]
            else:
                encode +=char
        print(f"encoded code is {encode}")
    # encrypt(text,shift)

    def decrypt(text,shift):
        decrypted_text = ""
        for char in text:
            if char in alphabet:
                char_index = alphabet.index(char)
                char_index -=shift
                if char_index <0:
                    char_index +=26
                decrypted_text +=alphabet[char_index]
            else:
                decrypted_text +=char
        print(f"decoded code is {decrypted_text}")

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Wrong input")
# decrypt(text,shift)

print(logo.logo)
while boolean:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction,text, shift)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'").lower()
    if repeat == "yes":
        boolean = True
    else:
        boolean = False
        print("GoodBye")
