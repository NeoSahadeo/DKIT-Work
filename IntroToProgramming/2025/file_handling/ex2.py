file = open("sample1", "r")

file_list = []

for x in file.readlines():
    file_list.append(x)

new_file = ""

for x in reversed(file_list):
    new_file += x

file.close()

file = open("sample1", "w")

file.write(new_file)
file.close()

