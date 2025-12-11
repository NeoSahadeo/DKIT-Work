AMOUNT_OF_GRADES = 6
grades = []


for x in range(AMOUNT_OF_GRADES):
    grade_input = int(input("Enter a grade: "))
    while grade_input < 0 or grade_input > 100:
        print("Invalid grade, please enter another one!")
        grade_input = int(input("Enter a grade: "))

    grades.append(grade_input)

print(grades)
