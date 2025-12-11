import math

type_number = True
contains_decimal = False

number = input("Enter a decimal number: ")
decimal_part = ''

for x in number:
    if contains_decimal:
        decimal_part += x

    if x == '.':
        contains_decimal = True
    elif x != '.' and x.isalpha():
        type_number = False
        break


if contains_decimal and type_number:
    print(decimal_part)
else:
    print("Number is not a decimal")

