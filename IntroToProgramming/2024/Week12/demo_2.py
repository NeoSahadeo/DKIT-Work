print("Please enter your grades for semester 1: ")

grades = []

for i in range(6):
    new_grade = int(input("Please enter a grade: \n"))
    grades.append(new_grade)

print("Thank you!")

for i in range(len(grades)):
    print(f"Grade {i + 1} = {grades[i]}")

print(f"Here are you grades: {grades}")

