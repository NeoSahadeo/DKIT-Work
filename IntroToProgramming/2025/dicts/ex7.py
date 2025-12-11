data_dict = {
    "name": "John",
    "age": "30",
    "city": "New York",
}


with open('output.txt', 'w') as file:
    for key, value in data_dict.items():
        print(f"Writing: {key}: {value}")
        file.write(f"{key}: {value}\n")


print("Data written to output.txt")

new_dict = {}

with open('output.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split(": ")
        new_dict[key] = value

print("Dictionary read from the file: ")
print(new_dict)






