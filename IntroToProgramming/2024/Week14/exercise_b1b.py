org_name = ""

firstname = input("Firstname: ")
lastname = input("Lastname: ")

if firstname.isalpha() and lastname.isalpha():
    org_name += firstname

    if len(lastname) <= 5:
        org_name += lastname
    else:
        org_name += lastname[:5]

    print(org_name)
else:
    print("First and last names can only contains letters")
