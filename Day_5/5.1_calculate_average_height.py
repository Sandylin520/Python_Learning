# 觀念:
# fruits = ["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

#way_1 用for loop來查找平均值，過程中不使用python 內建使用函數len(), sum()
student_heights = input("Input a list of student heights ").split()
total_height = 0
student_number = 0
for height in student_heights:
    #將輸入的學生身高的字串資料型態轉成int類型儲存到陣列中
    total_height += int(height)
    student_number += 1
    average_height = round(total_height/student_number)
print(average_height)#印出所有學生身高


# Way_2 查找平均值，直接使用函數len(), sum()
# for n in range(0,len(student_heights)):
#     #將輸入的學生身高的字串資料型態轉成int類型儲存到陣列中
#     student_heights[n] = int(student_heights[n])
#     total_height = sum(student_heights)
#     number_of_students = len(student_heights)
#     average_height = round(total_height/number_of_students)
# print(average_height)