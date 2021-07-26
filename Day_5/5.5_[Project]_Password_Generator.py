"""
random.choice(sequence)
- The choice() method returns a randomly selected element from the specified sequence.

random.choices(sequence, weights=None, cum_weights=None, k=1)
- k  Optional. An integer defining the length of the returned list

string.join(iterable)
- The join() method takes all items in an iterable and joins them into one string.
- ex: ''.join(password)

for i in range(5):
    print("hello world")
"""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


"""
Step 1: Use += to concaternate letters, numbers, symbols to empty string

password = "" #創建一個空陣列
for char in range(nr_letters):
    # random_char = random.choice(letters)
    # password += random_char
    password += random.choice(letters)
for char in range(nr_letters):
    password += random.choice(numbers)
for char in range(nr_letters):
    password += random.choice(symbols)
print(password)

"""


# # When you turn password from an empty string to a list, need to use list methods to add items
# password_list = []
# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
# print(f"Before shuffle: {password_list}")
# random.shuffle(password_list)
# print(f"After shuffle: {password_list}")

# # How to turn a list back to a string?  Use for loop
# password = ""
# for char in password_list:
#     password += char
# print(f"Your password is {password}")



"""
# Other solutions:
password = []
password.extend(random.choices(letters, k=nr_letters))
password.extend(random.choices(numbers, k=nr_numbers))
password.extend(random.choices(symbols, k=nr_symbols))
random.shuffle(password)
print(''.join(password))



# Other solutions:
password = []
for letter in range(nr_letters):
    password.append(random.choice(letters))
for symbol in range(nr_symbols):
    password.append(random.choice(symbols))
for number in range(nr_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)
new_password = ""
for i in password:
    new_password += i
print(f"Here is your password: {new_password}")

"""