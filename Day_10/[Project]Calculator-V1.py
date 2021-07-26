logo = ("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|


""")

import os
def clear(): os.system('cls') #on Windows System

#calculator
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

# Create a dictionary keys = operation, values = names of function
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def takeOperation():
    operation_symbol = input("Pick on an operation")
    #If input is invalid, go back to beginning of function
    if operation_symbol not in operations.keys():
        print("Invalid input. Please select an operation from given choices")
        return takeOperation()
    return operation_symbol

print(logo)
num1 = float(input("What's the first number? "))

should_continue = True
while should_continue:
    for symbol in operations:#print("+\n-\n*\n/\n")
        print(symbol)
    #operation_symbol = input("Pick on an operation: ")
    #add more check for operation
    operation_symbol  = takeOperation()
    # store a calculation function in the variable
    calculation_function = operations[operation_symbol]
    try:
        num2 = float(input("What's your next number? "))
        #print(type(calculation_function)) <class 'function'>
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    except ZeroDivisionError:
        print("A zerDivisionError Occured.")
        break
    #ask if user want to continue or not
    if input(f" Type 'y' to continue calculating with {answer},\
    or type 'n' to start a new calculation").lower() == "y":
    #Assigning answer to num1 because we want to use num1 variable for each step in while loop
        num1 = answer
        clear()
    else:
        should_continue = False
        print("GoodBye")


#Note:
#recusion - recalling the function within its own definition
#setting a flag, using a while loop to continue some piece of code execution




# Note:
# you can store a function in a variable without the parentheses
# at the end of that function and the function must be defined already
#
# calculation_function = operations[operation_symbol]