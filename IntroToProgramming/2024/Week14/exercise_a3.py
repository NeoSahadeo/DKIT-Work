org_name = ""

firstname = input("Firstname: ")
lastname = input("Lastname: ")

org_name += firstname

if len(lastname) <= 5:
    org_name += lastname
else:
    org_name += lastname[:5]

print(org_name)
