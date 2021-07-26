
"""
Instructions
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
"""

name01 = input("Please enter your name ")
name02 = input("Plese enter another party's name ")
combine_string = name01 + name02
checkname = combine_string.lower()
checktrue = checkname.count("t") + checkname.count("r") + checkname.count("u") + checkname.count("e")
checklove = checkname.count("l") + checkname.count("o") + checkname.count("v") + checkname.count("e")
lovescore = int(str(checktrue) + str(checklove))


if lovescore < 10 or lovescore > 90:
    print(f"Your score is  {lovescore}, you go together like coke and mentos.")
elif lovescore >= 40 and lovescore <= 50:
    print(f"Your score is {lovescore}, you are alright together")
else:
    print(f"Your score is {lovescore}")
