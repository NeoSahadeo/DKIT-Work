from exA1 import pretty_print


with open(input("Enter a file to read: "), "r") as file:
    data = []
    for x in file:
        data.append(x.strip())

pretty_print(data)

