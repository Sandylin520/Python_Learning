"""
Instructions
     1     2      3
1 ['⬜️', '⬜️', '⬜️']
2 ['⬜️', '⬜️', '⬜️']
3 ['⬜️', '⬜️', '⬜️']

"""

row1 = ["  ","  ","  "]
row2 = ["  ","  ","  "]
row3 = ["  ","  ","  "]

# 3*3的二維陣列
map = [row1,row2,row3]

position = input("where do you want to put the treasure?")

#這是一個3*3的二維陣列，x,y座標index起始值都是0,故都要-1
#字串的第一項是你選的x座標，因為是input是string資料型態，要轉成int才能-1
column = int(position[0])-1
row = int(position[1])-1

selected_row = map[row]
selected_row[column] = " x "

# 印出棋盤
print(f"{row1}\n{row2}\n{row3}")

