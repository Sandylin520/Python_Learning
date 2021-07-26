import random

random_integer = random.randint(1,10)# 1~10
print(random_integer)

random_float = random.random() #floating point number between [0.0 to 1.0]
print(random_float * 5) #0.000000....~ 4.9999999.....

love_score = random.randint(1,100)# 1~100
print(f"You love score is {love_score}")