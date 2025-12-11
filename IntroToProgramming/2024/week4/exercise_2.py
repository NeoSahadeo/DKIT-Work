number_1 = int(input("Please enter a number: "))
number_2 = int(input("Please enter another number: "))
operation = input("Enter the symbol for operation (+,-,/,*): ")

if operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
elif operation == "*":
    print(number_1 * number_2)
elif operation == "/":
    print(number_1 / number_2)
