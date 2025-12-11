from ex8 import print_dict

# Write a program that contains two dictionaries of phone contacts. In each dictionary, the key is the contact name
# and the value is the contact’s phone number.
# The program should combine these two dictionaries into a single dictionary and display it to the user. You should
# not consider the possibility of conflicts (where a key appears in both dictionaries) in this program.

contacts_1 = {
    "Neo SS": "0873569210",
    "John Smith": "0876543210",
    "Jane Doe": "0881234567",
    "Mike Johnson": "0898765432",
    "Emily Davis": "0865432109",
}
contacts_2 = {
    "William Brown": "0854321098",
    "Sara Wilson": "0843210987",
    "David Clark": "0832109876",
    "Emma Taylor": "0821098765",
    "Chris Lee": "0810987654"
}

for x, (key, value) in enumerate(contacts_2.items()):
    contacts_1[key] = value

print_dict(contacts_1)
