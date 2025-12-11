from summer import sumit

numbers = input("Enter some numbers, seperated by spaces: ").strip()
num_array = numbers.split(' ')
num_int_array = []

for x in num_array:
    if not x == '' and not x.isalpha():
        num_int_array.append(float(x))

total = sumit(num_int_array)

print(f"The sum is: {total}")
