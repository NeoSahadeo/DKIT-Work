import random

random_numbers = []
for x in range(0, 20):
    random_numbers.append(random.randint(1, 10))

print(random_numbers)

user_input = int(input("Enter a number to search for in the list: "))

if user_input in random_numbers:
    reversed_list = []
    for x in range(0, len(random_numbers)):
        reversed_list.append(random_numbers[len(random_numbers) - 1 - x])

    print(len(random_numbers) - reversed_list.index(user_input))
