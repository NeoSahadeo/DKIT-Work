# Free errors
# with open('week2.py') as file:
#     file_content = file.read()
# print(file)  # This would raise a NameError

# if int(input("How old are you: ")) >= 18:
#     print("Drinks are on you!")


age = int(input("How old are you: "))
drink_order = None

if age >= 21:
    drink_order = input("What's your order?")

if (drink_order != None):
    print(f"One {drink_order}, coming up!")
else:
    print(f"One soda, coming up!")
