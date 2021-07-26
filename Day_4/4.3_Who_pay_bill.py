import random
#1st way
name_string = input("Give me everybody's name, separated by a comma ")
list = name_string.split(",")
payer = list[(random.randint(0,len(list)-1))]
print( f"{payer} would pay the bill")

#2nd way,  use random.choice()
# name_string = input("Give me everybody's name, separated by a comma ")
# list = name_string.split(",")
# payer = random.choice(list)
# print( f"{payer} would pay the bill")