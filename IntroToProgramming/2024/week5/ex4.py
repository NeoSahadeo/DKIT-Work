number_1 = int(input("Please enter a number: "))
number_2 = int(input("Please enter another number: "))
operation = input("Please enter the math operation (+,-,*,/): ")

match operation:
    case "/":
        print(f"Answer?: {number_1 / number_2}")
    case "+":
        print(f"Answer?: {number_1 + number_2}")
    case "-":
        print(f"Answer?: {number_1 - number_2}")
    case "*":
        print(f"Answer?: {number_1 * number_2}")
    case _:
        print("Operation not supported")
