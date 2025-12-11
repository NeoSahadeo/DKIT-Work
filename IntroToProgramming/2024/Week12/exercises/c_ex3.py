numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(numbers)

user_input = int(input("Enter a position to delete: "))

if user_input >= 0 and user_input < len(numbers):
    print(f"Deleting: {numbers[user_input]}")
    numbers.pop(user_input)
    print(numbers)
else:
    print("Position is invalid and cannot be delete.")
