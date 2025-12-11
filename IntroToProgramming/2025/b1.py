def pretty_print(elements):
    for i in range(0, len(elements)):
        print(f"{i}) {elements[i]}")


amount = int(input("How many items: "))
user_list = []

for i in range(0, amount):
    x = input("Enter something: ")
    user_list.append(x)

pretty_print(user_list)
