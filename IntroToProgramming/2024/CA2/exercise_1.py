# Exercise 1 - Neo Sahadeo 07.11.2024
import random


# Takes the user input of how many
# numbers they want the program to
# create.
amount_of_nums = int(input("Enter the amount of numbers you would like to create: "))
amount_of_even_nums = 0  # Only tracking even number because odd numbers can be calculated using the difference.
largest_num = -1  # Set largest_num to -1 because I find it easier to find errors in the code.
total = 0

# Loop through the range of [0, amount_of_nums)
for x in range(0, amount_of_nums):
    # random.randint() will give me a random
    # value n between a and b (random — Generate pseudo-random numbers n.d.)
    # such that a <= n <= b or [1, 100]
    random_number = random.randint(1, 100)
    total += random_number

    # Check if the current largest number is larger than
    # the newly generated number.
    if (random_number > largest_num):
        largest_num = random_number

    # I use Python's in-built modulus operator
    # to evaluate if the random number is even or
    # odd. Python has truthiness so I don't need
    # to explicitly check if the value is equal to
    # zero.
    if (random_number % 2):
        print(f"Gen: {random_number} -> odd")
    else:
        print(f"Gen: {random_number} -> even")
        amount_of_even_nums += 1

print(f"""
Total Even Numbers Gen: {amount_of_even_nums}
Total Odd Numbers Gen: \t{amount_of_nums - amount_of_even_nums}
Largest Number: \t{largest_num}
Average value: \t\t{total / amount_of_nums:0.0f}
""")

# References:
# random — Generate pseudo-random numbers. Python documentation [online]. Available from: https://docs.python.org/3/library/random.html [accessed 7 November 2024].
