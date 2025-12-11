def highest_grade(grades):
    highest_grade = -1
    for i in grades:
        if highest_grade < i:
            highest_grade = i

    print(highest_grade)



grades = []
num_grades = int(input("How many grades do you want to enter: "))

for i in range(num_grades):
    grade = int(input(f"Please enter the next grade: "))
    grades.append(grade)

print(f"Grades entered: {grades}")

highest_grade(grades)
