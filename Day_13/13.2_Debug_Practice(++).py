# # Practice_6: Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

"""
Use a Debugger 題目分析
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)
  print(a_list)
mutate([1,2,3,5,8,13])

# mutate 是一個function物件，這個function傳入一個叫a_list的list,
# 於是mutate這個物件中有新的變數a_list
# create b_list 變數，是個空陣列
# 迴圈走訪a_list *2，又產生一個新變數new_item
# b_list.append(new_item) 只會將迴圈走訪到的最後一個new_item存入b_list
# print(b_list)  [26]   故最後印出b_list只會印出陣列中只有一個項目
# print(a_list) [1, 2, 3, 5, 8, 13]  仍舊印出所有陣列項目

"""
#Practice_6: solution
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)#[2, 4, 6, 10, 16, 26]
mutate([1,2,3,5,8,13])
