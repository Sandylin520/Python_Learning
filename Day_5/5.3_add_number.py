#add 1~100
total = 0
for number in range(1,101):
    total += number
print(total)

#calculate the sum of all the even number from 1 to 100
#way_1
total = 0
for number in range(2,101,2):
    total += number
print(total)

#way_2
total2 = 0
for number in range(1,101):
    if number % 2 == 0:
        total2 += number
print(total2)
