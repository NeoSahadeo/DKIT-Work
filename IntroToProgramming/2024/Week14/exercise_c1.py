AMOUNT = 10

contains_is = 0

for x in range(0, AMOUNT):
    text = input("Enter some text: ")
    if text.find("is") > -1:
        contains_is += 1

print(contains_is)
