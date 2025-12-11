org_name = ""

full_name = input("Enter first and lastname: ").strip()
name_array = full_name.split()
firstname = name_array[0]
lastname = name_array[1]

org_name += firstname

if firstname.isalpha() and lastname.isalpha():
    if len(lastname) <= 5:
        org_name += lastname
    else:
        org_name += lastname[:5]
    print(org_name)
else:
    print("Only letters are allowed!")
