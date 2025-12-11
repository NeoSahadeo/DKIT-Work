# Write a program that contains a hard-coded dictionary of phone contacts (key: contact name, value: contact
# number) populated with dummy data. Your program should:
# • Ask the user to enter the name of the contact they wish to view.
# • Retrieve the corresponding phone number for that contact and display it to the user.
# Your program should not handle where the contact name is not present in the dictionary.

contacts = {
    "Neo SS": "0873569210",
    "John Smith": "0876543210",
    "Jane Doe": "0881234567",
    "Mike Johnson": "0898765432",
    "Emily Davis": "0865432109",
    "William Brown": "0854321098",
    "Sara Wilson": "0843210987",
    "David Clark": "0832109876",
    "Emma Taylor": "0821098765",
    "Chris Lee": "0810987654"
}

search = input("Search Contacts: ").strip()
result = contacts.get(search)

if result:
    print(f"Contact found for {search}: {result}")
# B1
else:
    print(f"Contact {search} was not found.")
