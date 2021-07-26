print("Welcome to the tip")
bill = float(input("what is the total bill?"))
tip = int(input("what percentage tip would you like to give? 10,12,or 15? $" ))
people = int(input("How many people to split the bill?"))
bill_with_tip = bill*(1+ tip/100)
print(f"Your total bill is {bill_with_tip}")
bill_per_person = bill_with_tip/people
#四捨五入
paid_by_each_person = round(bill_per_person,2)
#確保最後輸出到小數點第二位
paid_by_each_person = "{:.2f}".format(bill_per_person)
#print(paid_by_each_person)
print(f"Each Person should pay: {paid_by_each_person}")