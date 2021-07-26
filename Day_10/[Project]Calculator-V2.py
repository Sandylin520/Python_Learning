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

#used lambda functions for the mathematical operations

#adding
add = lambda x,y: x + y

#subtracting
subtract = lambda x,y: x-y

#multilpy
multiply = lambda x,y: x*y

#dividing
divide = lambda x,y: x/y


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def takeOperation():
    operation_symbol = input("Please enter your operation")
    if  operation_symbol not in operation.keys():
        print("invalid input")
        return takeOperation()
    return operation_symbol


print(logo)
should_continue = True
num1 = float(input("What's the first number? "))
for key in operation:
    print(key)
    #operation_symbol = input("Please enter your operation")
operation_symbol = takeOperation()
while should_continue:
    num2 = float(input("What's your seocnd number? "))
    #save the function result in variable answer
    #print(type(calculate_function)) <class 'function'>
    try:
        answer = operation[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    except ZeroDivisionError:
        print("A zerDivisionError Occured.")
        break
    #ask whether user would like to continue or not
    continue_calculation = input("Type 'y' to continue calculating with {answer}, or type 'n' to exit:")
    if continue_calculation == "y":
        num1 = answer
        clear()
    else:
        clear()
        should_continue = False
        print("Goodbye")




