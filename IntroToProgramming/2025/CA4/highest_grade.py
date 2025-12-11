# Neo Sahadeo - 07/10/2025

grades = input("Enter grades: ").split()
highest_grade = -1
for x in grades:
    if highest_grade < int(x):
        highest_grade = int(x)

print(highest_grade)
