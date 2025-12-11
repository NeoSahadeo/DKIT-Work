from ex4_function import adder

amount_of_numbers = int(input("How many numbers do you want to add up?: "))


list_of_numbers = []
for number in range(0, amount_of_numbers):
    user_input = int(input(f"Enter a number({number + 1}): "))
    list_of_numbers.append(user_input)

adder(list_of_numbers)
