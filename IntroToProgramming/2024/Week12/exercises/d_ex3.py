AMOUNT = 10

numbers = []

for x in range(0, 10):
    numbers.append(int(input("Enter a number: ")))

numbers.sort()
print("Ascending: ", numbers)
numbers.sort(reverse=True)
print("Descending: ", numbers)
print("Maximum value: ", max(numbers))
print("Minimum value: ", min(numbers))
