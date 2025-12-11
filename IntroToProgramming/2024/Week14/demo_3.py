MINIMUM_LENGTH = 8

# This is to check if the password length meets the minimum
password_length = False

contains_letter = False
contains_digit = False


password = input("Password: ")

if len(password) >= MINIMUM_LENGTH:
    password_length = True

for x in password:
    if (x.isalpha()):
        contains_letter = True
    if (x.isdigit()):
        contains_digit = True

if password_length and contains_letter and contains_digit:
    print("Password Valid!")
elif not contains_letter:
    print("Does not contain any letters!")
elif not contains_digit:
    print("Does not contain any numbers!")
elif not password_length:
    print(f"{password} must be at least 8 characters long!")
else:
    print("Error occured")
