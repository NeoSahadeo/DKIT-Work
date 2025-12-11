values = []

print("Number Summer, type 'sum' to sum all the numbers")

while True:
    user_input = input('Enter an integer: ')

    if (user_input == 'sum'):
        break

    values.append(int(user_input))

print(f"""
Total: {sum(values)}
Average: {sum(values) / len(values)}
Max: {max(values)}
Min: {min(values)}
""")
