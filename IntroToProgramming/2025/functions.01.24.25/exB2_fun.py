def valid_number(phone_number):
    prefix = phone_number[0:3]
    if prefix == "087" and len(phone_number) == 10:
        print(f"{phone_number} is valid")
    else:
        print(f"{phone_number} is invalid")
