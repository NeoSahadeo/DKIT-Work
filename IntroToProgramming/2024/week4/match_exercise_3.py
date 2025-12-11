number_one = float(input("Please enter a number: "))
number_two = float(input("Please enter another number: "))
operation = input("Please enter a mathematical operation (+, /, -, *): ")

match operation:
    case "+":
        print(f"Answer?: {number_one + number_two}")
    case "-":
        print(f"Answer?: {number_one - number_two}")
    case "/":
        print(f"Answer?: {number_one / number_two}")
    case "*":
        print(f"Answer?: {number_one * number_two}")
