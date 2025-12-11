user_input = int(input("Even numbers till: "))

for x in range(0, user_input, 2):
    if x == 0:
        continue
    print(x)
