# Creates a blank users dictionary.
# • Reads in your user data file and stores each line as a list of user information. Each list of user data should
# be stored in the users dictionary. When storing each line of data, the key should be the username for that
# line, and the value should be the list of user information.
# • When adding to the dictionary, you should confirm the username doesn’t already exist before you add a
# new user’s information.

def add_to_dict(key, data, dict_name):
    result = dict_name.get(key)
    if not result:
        user_data[key] = data
        return True
    return False


user_data = {}

with open("exC1.csv", "r") as file:
    for line in file:
        line = line.split(",")
        data = []
        for x in line:
            data.append(x.strip())
        user_data[data[0]] = data[1:]

username = input("Username: ")
password = input("Password: ")
firstname = input("Firstname: ")
lastname = input("Lastname: ")

if add_to_dict(username, [password, firstname, lastname], user_data):
    print("Added to dictionary")
else:
    print("Value already exists in dictionary")

