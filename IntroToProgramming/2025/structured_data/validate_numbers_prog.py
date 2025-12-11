from validate_number import validate

if __name__ == "__main__":
    data = []  # Data will store my numbers and names

    # Open the file and add the lines to the data list
    with open("sign_ups", "r") as file:
        for x in file:
            data.append(x.strip())
        file.close()

    # Sort the data into numbers and names
    sort_nums = []
    sort_names = []
    for x in data:
        data_split = x.split(",")
        sort_names.append(data_split[0])
        sort_nums.append(data_split[1])

    # Validate the data
    valid_nums = []
    valid_names = []
    for x in range(0, len(sort_nums)):
        if validate(sort_nums[x]):
            valid_nums.append(sort_nums[x])
            valid_names.append(sort_names[x])
        else:
            print(f"Invalid Number: {sort_names[x]} - {sort_nums[x]}")
            valid_nums.append(None)
            valid_names.append(None)

    # Write out data to files
    with open("valid_names", "w") as file:
        for x in valid_names:
            if x:
                file.write(x + "\n")

    with open("valid_nums", "w") as file:
        for x in valid_nums:
            if x:
                file.write(x + "\n")

    # valid_names = []
    # valid_nums = []
    # with open("valid_names", "r") as name_file:
    #     for x in name_file:
    #         valid_names.append(x)
    #
    # with open("valid_nums", "r") as num_file:
    #     for x in num_file:
    #         valid_nums.append(x)
    #
    # for x in range(0, len(valid_names)):
    #     print(f"{valid_names[x].strip()}: {valid_nums[x].strip()}")
