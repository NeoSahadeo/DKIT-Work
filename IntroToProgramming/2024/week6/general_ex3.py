total = 0

while True:
    user_input = float(input("Enter a number: "))

    if user_input > 0:
        total += user_input
    else:
        break

print(total)
