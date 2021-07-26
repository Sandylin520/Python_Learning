#leap year
#on every year that is evenly divisible by 4
#except every year that is evenly divisible by 100 (except不包含此狀況 year % 100!=0 才會是leap yr)
# unless the year is also evenly divisible by 400 (unless 包含此狀況)
#way_1
year = int(input("which year do you want to check"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:#可以被400整除
            print("leap year")
        else:
            print("Not a leap year")
    else:#可以被4整除，不能被100整除
        print("leap year")
else:
    print("not a leap year")

#way_2
year = int(input("which year do you want to check"))
if (year % 4 == 0  and year % 100 != 0) or (year % 400 ==0 ):
     print(f"{year} is a leap year")
else:
     print(f"{year} is not a leap year")