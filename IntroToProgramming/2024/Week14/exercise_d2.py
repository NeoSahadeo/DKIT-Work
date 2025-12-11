special_symbols_array = ["?","!","#","%","*"]

g_present = False
first_three_not_x = False
contains_digit = False
special_symbol = False
eight_chars = False


password_input = input("Password: ")

if password_input[0:3] != 'xxx':
    first_three_not_x = True

if len(password_input) >= 8:
    eight_chars = True

for x in password_input:
    if x == 'G':
        g_present = True
    elif x.isdigit():
        contains_digit = True
    elif x in special_symbols_array:
        special_symbol = True

if g_present and first_three_not_x and contains_digit and special_symbol and eight_chars:
    print("Password Valid")
else:
    print("Password Invalid")
