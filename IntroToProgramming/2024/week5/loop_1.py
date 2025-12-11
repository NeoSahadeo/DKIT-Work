sum = 0
for i in range(3):
    if i == 0:
        sum += int(input("Please enter your first grade: "))
    if i == 1:
        sum += int(input("Please enter your second grade: "))
    if i == 2:
        sum += int(input("Please enter your third grade: "))

print(f"Sum: {sum}")
print(f"Average grade: {sum/3}")
