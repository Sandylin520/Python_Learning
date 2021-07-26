# way_1 使用for loop計算最大值，不使用python內建max()
student_scores = input("Input a list of student scores: ").split()
highest_score = 0
for score in student_scores:
    score = int(score)
    if score > highest_score:
       highest_score = score
print(highest_score)


# # way_2 查找最大值，使用python內建函數max()
# student_scores = input("Input a list of student scores: ").split()
# for n in range(0,len(student_scores)):
#     #將輸入的字串型態陣列項目轉為int存入各個陣列項目中
#     student_scores[n] = int(student_scores[n])
# highest_score = max(student_scores)
# print(highest_score)
