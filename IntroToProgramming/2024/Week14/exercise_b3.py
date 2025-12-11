text = input("Enter some text: ")

uppercase = 0
lowercase = 0
space = 0
number = 0

for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isnumeric():
        number += 1
    elif char == ' ':
        space += 1

print(f"""
Uppercase: {uppercase}
Lowercase: {lowercase}
Space: {space}
Number: {number}
      """)
