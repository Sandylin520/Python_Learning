"""
Problem 1
Handle the exception thrown by the code below by using try and except blocks.

for i in ['a','b','c']:
    print(i**2)
"""


try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("General error!catch out!")

"""
Problem 2
Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 0
z = x/y
"""

try:
    x = 5
    y = 0
    z = x/y
except:
        print("Error")
finally:
        print('All Done.')

"""
Problem 3
Write a function that asks for an integer and prints the square of it.
Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    pass
ask()

"""

#Solution 1
def ask():
    while True:
        try:
            number = int(input("Input an integer:"))**2
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            break
    print(f"Thank you, your number squared is:{number}")

ask()



# Solution 2
def ask():
    waiting = True
    while waiting:
        try:
            number = int(input("Input an integer:"))**2
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            waiting = False
    print(f"Thank you, your number squared is: {number}")

ask()