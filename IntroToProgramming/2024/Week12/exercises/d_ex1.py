numbers = []

while True:
    user_input = input("Enter a floating number (or type 'quit' to quit): ")
    if user_input == 'quit':
        break

    numbers.append(float(user_input))

print(f"""
Avg: {sum(numbers) / len(numbers)}
""")
