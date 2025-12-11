# Neo Sahadeo 16/10/2024

# Create 3 variables
# placeholder is for the swap
placeholder = 0
num1 = int(input("Enter number 1: "))  # take in the first number
num2 = int(input("Enter number 2: "))  # take in the second number

# Copy the value from num1 to placeholder
placeholder = num1

# Copy the value from num2 to num1
num1 = num2

# Copy the placeholder value (which is num1) to num2
num2 = placeholder

# Display the numbers
print(f"\nNumber 1: {num1}\nNumber 2: {num2}")
