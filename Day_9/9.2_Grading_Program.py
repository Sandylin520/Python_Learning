"""
Instructions
You have access to a database of student_scores in the format of a dictionary.
The keys in student_scores are the names of the students and the values are
their exam scores.

Write a program that converts their scores to grades. By the end of your program,
you should have a new dictionary called student_grades that should contain
student names for keys and their grades for values. The final version of the
student_grades dictionary will be checked.

This is the scoring criteria:
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"

"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

#Create an empty dictionary
student_grade = {}

#Add the grades
for student in student_scores:
    # get student's grade 取每個student 的value(分數)
    score = student_scores[student]
    if score > 90:
        #give key and value to student_grad key = value
        student_grade[student] = "Outstanding"
    elif score > 80:
        student_grade[student] = "Exceeds Expectations"
    elif score > 70:
        student_grade[student] = "Acceptable"
    else:
        student_grade[student] = "Fail"

    # if score <= 70:
    #       student_grade[student] = "Fail"
    # elif score <= 80:
    #       student_grade[student] = "Acceptable"
    # elif score <= 90:
    #       student_grade[student] = "Exceeds Expectations"
    # else:
    #       student_grade[student] = "Outstanding"
print(student_grade)


