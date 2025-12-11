# Exercise 2 - Neo Sahadeo 07.11.2024

# Set the maximum amount of attempts
# and the default state of the system.
ATTEMPTS = 3
LOGGED_IN = False

login_attempts = 0  # keep track of failed logins
print("Woodle - Login")

# Loop n(ATTEMPTS) amount of times.
for x in range(0, ATTEMPTS):
    # Update the login attempts
    login_attempts += 1

    # Take in the user's username and password
    username = input("Username: ")
    password = input("Password: ")

    # Check if the username and password match
    if (username == "user001" and password == "p455W0rd"):
        LOGGED_IN = True  # update the state of the system
        break  # jump out of the loop

if LOGGED_IN:
    print(f"Welcome back to Woodle. (Login attemps: {login_attempts})")
else:
    print("Login Failed! Too many attempts, account has been locked.")
