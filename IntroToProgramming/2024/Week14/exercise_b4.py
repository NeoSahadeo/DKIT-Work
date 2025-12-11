text = input("Enter some text: ")

buffer = ""

for char in text:
    if char.isalpha() and char.islower():
        buffer += char.upper()
    elif char.isalpha() and char.isupper():
        buffer += char.lower()
    else:
        buffer += char

print(buffer)
