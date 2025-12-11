# Neo Sahadeo - 10/10/2025

grades = input("Enter grades: ").split()
total = 0
length = 0
for x in grades:
    total += int(x)
    length += 1

print(f"Average: {total / length}")
