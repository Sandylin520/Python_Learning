#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

import os
def clear(): os.system('cls') #on Windows System

from art import logo
print(f"\033[31m{logo}\033[00m")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    #shift_amount必須維持為負數，故要放在for loop外面
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        #預防使用中輸入極大值的Index導致index out of bound
        while new_position >= 26:
            new_position -=26
        while new_position  < 0:
            new_position += 26
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")


end_the_game = False
while not end_the_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    restart = input("Would you like to restart the cipher program? Please enter yes or no ").lower()
    #if 要寫在while裡面才能接收到restart的結果
    if restart == "no":
        end_the_game = True
        print("Goodbye")
    else:
        clear()
"""
def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for index in range(len(text)):
        #找到對應alphabet的index值
        position = alphabet.index(text[index])
        #將對應的alphabet的index值進行位移
        cipher_index = position+shift
        if cipher_index > 25:
            cipher_index -=26
        new_letter = alphabet[cipher_index]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text,shift_amount):
    decrypted_word = ""
    for index in range(len(cipher_text)):
        position = alphabet.index(cipher_text[index])
        decrypted_word_index = position-shift
        if decrypted_word_index <0 :
            decrypted_word_index +=26
        new_letter = alphabet[decrypted_word_index]
        decrypted_word += new_letter
    print(f"The decoded text is {decrypted_word}")

if direction == "encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text,shift_amount=shift)

"""


"""
ANSI colors

print(f"\033[31m{logo}\033[00m")
\033[31m = foreground color RED
\033[00m = resets all colors after, or else everything will show red :)

"""