#EX1:
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#下面resources不需要宣告global用[],會一個個進去找
def deduct_ingredient():
    resources["water"] -= 5

print(resources["water"])#300
deduct_ingredient()
print(resources["water"])#295


#EX2:
#下列profit若沒有加global字樣會報錯!python會把profit當區域變數
def check_transaction_successful():
    global profit
    profit += drink
    print(profit)#5

profit = 0
drink = 5
check_transaction_successful()
print("outside the function", profit)#5


#UnboundLocalError: local variable 'profit' referenced before assignment
# def check_transaction_successful():
#     profit += drink

# profit = 0
# drink = 5
# check_transaction_successful()