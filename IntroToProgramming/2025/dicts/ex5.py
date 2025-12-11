def save_data(file_name, name, number):
    data = parse_data(file_name)
    data[name] = number

    with open(file_name, "w") as file:
        for value in data.keys():
            file.write(f"{value},{data[value]}\n")


def parse_data(file_name):
    with open(file_name, "r") as file:
        data = {}
        for x in file:
            values = x.split(",")
            data[values[0].strip()] = values[1].strip()
    return data


if __name__ == "__main__":
    file_name = "phone_database.csv"
    data = parse_data(file_name)
    while True:
        name = input("Save name: ").strip()

        if name in data:
            print("Name already exists!")
        else:
            number = input("Enter phone number: ").strip()
            save_data(file_name, name, number)
            _continue = input("Save Another? (y/n): ").strip().lower()
            if _continue == 'n':
                break
            elif not _continue == 'y':
                print('Symbol not recognised, exiting!')
                break
