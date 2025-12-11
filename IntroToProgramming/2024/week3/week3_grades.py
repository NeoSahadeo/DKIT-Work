grade = int(input("Enter your grade (percentage): "))

if grade < 40:
    print("Fail")
elif grade < 50:
    print("Pass")
elif grade < 60:
    print("2.2 (Second class honours, grade 2)")
elif grade < 70:
    print("2.1 (Second class honours, grade 1)")
else:
    print("1.1 (First class honours), congratulations!")
