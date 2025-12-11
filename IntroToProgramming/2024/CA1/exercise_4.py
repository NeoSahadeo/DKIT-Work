# Neo Sahadeo 16/10/2024

# Ask the user to enter a password.
password = input("Enter password: ")

# DRY / Pytonic way to get length
# is to set a variable equal to it.
password_length = len(password)

# Check if the password is
# within this range [0, 6]
if password_length <= 6:
    print("Password is weak!")

# Check if the password is
# within this range (6, 10]
elif password_length > 6 and password_length <= 10:
    print("Password is medium!")

# Check if the password is
# within this range (10, inf]
else:
    print("Password is strong!")
