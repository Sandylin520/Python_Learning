from art import logo
print(f"\033[31m{logo}\033[00m")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text,shift_amount,direction_side):
    word = ""
    if direction == "decode":
        shift_amount *= -1
    for item in text:
        index_number = alphabet.index(item)
        position = index_number + shift_amount
        while position > 25:
            position -=26
        letter = alphabet[position]
        word += letter
    print(word)


end_of_game = False
#while game not end
while not end_of_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt :\n ")
    text = input("input your message:\n").lower()
    shift = int(input("type the shift number:\n"))
    caesar(plain_text=text,shift_amount=shift,direction_side=direction)
    exit = input("Do you want to exit the game? yes or no ")
    if exit == "yes":
        end_of_game = True
        print("Goodbye")

