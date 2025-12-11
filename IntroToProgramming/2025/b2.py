def valid_phone(text):
    if text[0:3] == "087" and len(text) == 10:
        print("Valid")
    else:
        print("Invalid")


numbers = []
for i in range(0, 10):
    numbers.append(input("Enter number: "))

for element in numbers:
    valid_phone(element)
