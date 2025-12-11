total = 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Normalise the numbers
if num1 < num2:
    num1, num2 = (num2, num1)

for x in range(num2, num1 + 1):
    total *= x

print("Sum: ", total)
