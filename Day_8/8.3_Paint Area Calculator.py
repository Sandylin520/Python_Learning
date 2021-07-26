import math
# 1 can of paint can cover 5 square meters of wall
wall_height = int(input("Input the height of wall: "))
wall_width = int(input("Input the width of wall: "))
coverage = 5

def paint_calc(height,width,cover):
    area = height * width
    num_of_cons = math.ceil(area/cover)
    print(f"You'll need {num_of_cons} cans of paint")

paint_calc(height=wall_height,width=wall_width,cover=coverage)

