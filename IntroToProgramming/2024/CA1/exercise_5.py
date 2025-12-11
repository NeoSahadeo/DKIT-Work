# Neo Sahadeo 16/10/2024

# Create a boolean flag to
# make boolean logic easier.
grade_valid = True

# Get the maths, history, and geography
# grades as integers
maths_grade = int(input("Grade for Maths: "))
history_grade = int(input("Grade for History: "))
geography_grade = int(input("Grade for Geography: "))

# Check if any of the grades are invalid.
# Valid grades [0, 100]
if maths_grade < 0 or maths_grade > 100 or history_grade < 0 or history_grade > 100 or geography_grade < 0 or geography_grade > 100:
    grade_valid = False

# Calculate grade average
grade_average = ((maths_grade + history_grade + geography_grade) / 3)

# Check if the grade is within [70, 100]
if grade_valid and grade_average >= 70:
    print(f"Your GPA was {grade_average:.0f}, well done!")

# Check if the grade is within (40, 70)
elif grade_valid and grade_average > 40:
    print(f"Your GPA was {grade_average:.0f}, good effort, but keep working")

# Check if the grade is within [0, 40]
else:
    print(f"Your GPA was {grade_average:.0f}, maybe see if you can study with a classmate?")
