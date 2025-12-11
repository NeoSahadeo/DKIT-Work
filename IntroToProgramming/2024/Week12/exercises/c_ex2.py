AMOUNT = 10


strings = []

for x in range(0, AMOUNT):
    strings.append(input("Enter something: "))

print("Deleting!!!!")

for x in range(0, AMOUNT):
    print(f"Deleting: {strings[-1]}")
    strings.pop()
