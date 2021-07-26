#TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
#TODO 3. Print report.
#TODO 5. Process coins.
#TODO 6. Check transaction successful?
#TODO 7. Make Coffee


from main import MENU,resources

profit = 0
def print_the_report(resources):
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${profit}")

def turn_off_machine():
    power_on = False
    return power_on

def check_resource_sufficient(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]: #get ingredients key's value
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def calculate_the_money_value():
    total = int(input("How many quarters($0.25) ? "))*0.25
    total += int(input("How many dimes($0.10) ? "))*0.10
    total += int(input("How many nickles($0.05) ? "))*0.05
    total += int(input("How many pennies($0.01) ? "))*0.01
    return total

def check_transaction_successful(money,drink):
    if money < drink:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:# money >= drink:
        change = round((money-drink),2)
        global profit
        profit += drink
        if money > drink:
            print(f"Here is your change {change}")
        return True

def make_coffee(coffee_ingredient):
    """Deduct the required ingredients from the resources."""
    for item in coffee_ingredient:
      # resource key's value -= coffee ingredient key's value
        resources[item] -= coffee_ingredient[item]
    print(f"Here is your {user_input}! Enjoy!!")

print("Power ON!")
print("options: ")
print("espresso")
print("latte")
print("cappuccino")
print("off")
print("current-stock")
print("update-stock")
print("----------------------------------------------------")
# while user enter report, print current resouce and ask
machine_on = True
while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == "off":
        machine_on = False
        print("Goodbye!")
    elif user_input == "current-stock":
        print_the_report(resources)
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        drink = MENU[user_input]
        #check ingredient sufficient or not
        result = check_resource_sufficient(drink["ingredients"])
        #if ingredient suffient enough, ask user to input coin
        if result == True:
            print("Please insert coins")
            money = calculate_the_money_value()
            #print(money)
            #check transaction succesful or not
            transaction_success = check_transaction_successful(money, drink["cost"])
            #print(transaction_success)
            if transaction_success:
                make_coffee(drink["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            add_resource = input("Do you want to add more resources? Enter 'y' or 'n' ").lower()
            if add_resource == 'y':
                resources["water"] += int(input("Add water (ml): "))
                resources["coffee"] += int(input("Add coffee (g): "))
                resources["milk"] += int(input("Add milk (ml): "))
    else:
        print("Please enter valid input")

#print(drink) #{'ingredients': {'water': 200, 'milk': 150, 'coffee': 24}, 'cost': 2.5}
#print(drink["ingredients"]) #{'water': 200, 'milk': 150, 'coffee': 24}
#print(drink["cost"])  #2.5



"""


"""