#under 18.5 they are underweight   <18.5
#over 18.5 but below  they have a normal weight 18.5<X<25
#over 25 but below 30 they are overwight  25<X<30
#pver 30 but below 35 they are obese  30<X<35
#above 35, they are clinically obese  X>35

height = float(input("enter your height in m:"))
weight = float(input("enter your weight in kg"))
#四捨五入取整數
BMI = round(weight/height**2)
if BMI < 18.5:
    print(f"your BMI is {BMI}, you are underweight")
elif BMI < 25:
    print(f"your BMI is {BMI}, you have a normal weight")
elif BMI < 30:
    print(f"your BMI is {BMI}, you are overweight")
elif BMI <35:
    print(f"your BMI is {BMI}, you are obese")
else:
    print(f"your BMI is {BMI}, you are clinically obese")