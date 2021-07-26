#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25

#Pepperoni for Small pizza: +$2
#Pepperoni for Medium or Large Pizza: +3
#Extra cheese for any size pizza: +$1

print("Welcome to Python Pizza Deliveries ")
size = input("what size pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_chesse = input("Do you want extra chesse? Y or N ")
bill = 0

if size == "S":
    bill += 15

elif size == "M":
    bill += 20

else:
    bill += 25

if add_pepperoni == "Y":
    if size == "5":
        bill += 2
    else:
        bill += 3

if extra_chesse == "Y":
    bill += 1

print(f"Your final bill is {bill}")

