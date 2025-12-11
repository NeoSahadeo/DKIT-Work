def generate_username(firstname, lastname):
    firstname = firstname[0:1]
    if len(lastname) > 5:
        lastname = lastname[0:6]

    print(f"Welcome: {firstname}{lastname}")
