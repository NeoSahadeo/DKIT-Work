# Neo Sahadeo - 11/10/2025

grades = input("Enter grades: ").split()
lowest = 101
for x in grades:
    if lowest > int(x):
        lowest = int(x)

print(lowest)
