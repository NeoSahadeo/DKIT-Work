def calc_avg(values):
    if len(values) > 0:
        avg = sum(values)/len(values)
        return avg

numbers = input("Enter some numbers, seperated by spaces: ").strip()
num_array = numbers.split(' ')
num_int_array = []

for x in num_array:
    if not x == '' and not x.isalpha():
        num_int_array.append(float(x))

avg = calc_avg(num_int_array)

print(f"The average of {num_int_array} is {avg}")
