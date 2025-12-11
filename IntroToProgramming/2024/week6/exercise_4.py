sum = 0
average = -1
max_range = int(input("How many numbers do you want to enter: "))
for x in range(0, max_range):
    sum += int(input(f"Enter number {x+1}: "))

print(f"""
Sum: \t {sum}
Avg: \t {sum/max_range}
""")