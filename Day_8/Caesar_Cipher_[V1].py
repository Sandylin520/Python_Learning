#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


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
