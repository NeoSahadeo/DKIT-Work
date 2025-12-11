import math


found = False
my_nums = [37, 92, 15, 68, 24, 53, 81, 6, 49, 43]
my_nums.sort()
value_wanted = 43

# Binary Search algo
low = 0
high = 10  # Array length
iterations = 0

while low < high:
    iterations += 1
    middle = math.floor(low + (high - low) / 2)

    if my_nums[middle] == value_wanted:
        found = True
        break

    if (my_nums[middle] > value_wanted):
        high = middle
    else:
        low = middle + 1

print(f'Iterations: {iterations}, {found}')
