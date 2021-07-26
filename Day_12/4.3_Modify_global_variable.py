"""
---不好的示範: 直接在方法內變更全域變數----

enemies = 1
def increase_enemies():
    global enemies
    enemies +=1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function:{enemies}")

#enemies inside function: 2
#enemies outside function:2

"""


#好的示範:  透過方法return結果+1，再存到全域變數中
enemies = 1
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function:{enemies}")

#enemies inside function: 1
#enemies outside function:2