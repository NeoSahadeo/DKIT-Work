items = {
    "names": ["amanda", "John"],
    "vegetables": ["carrot", "broccoli"],
    "animals": ["dog", "cat"],
    "numbers": [1, 3, 8]
}

items["names"].append("Mary")
items["vegetables"].append("lettuce")
items["animals"].append("mouse")
print(items)

items["colors"] = ["red", "blue"]
items["colors"].append("green")
print("New items added to the dictionary")
print("------------------------------------------------------------")

print(items)
name_list = items["names"]
print(name_list)
new_name = input("what name do whish to add: ")

items["names"].append(new_name)
print(items)
num_max = max(items["numbers"])
print(num_max)
