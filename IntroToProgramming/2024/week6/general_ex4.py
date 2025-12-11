import getpass

attempts = 3

username = "HelloKitty"
password = "PrettyBow1"

while True:
    user_username = input("Username: ")
    user_password = getpass.getpass("Password: ")

    if user_username == username and user_password == password:
        print("Log in successful")
        break

    if attempts > 0:
        attempts -= 1
        print(f"Credentials invalid, attemps left: {attempts}")
