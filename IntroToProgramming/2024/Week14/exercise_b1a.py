AMOUNT = 10

phone_numbers = []

for x in range(0, AMOUNT):
    number = input("Enter a phone number: ")
    if not number.isnumeric():
        print("Number entered contains a string.")
        break

    if len(number) == 10:
        phone_numbers.append(number)
    else:
        print('Invalid phone number entered!')
        break


counter = 0  # Counter will track how many times 087 is entered
for number in phone_numbers:
    if number[:3] == "087":
        counter += 1

print(f"087 appears {counter} amount of times.")
