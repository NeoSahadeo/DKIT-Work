from exB2_fun import valid_number

phone_reg = []
for x in range(0, 10):
    phone_reg.append(input(f"Phone number({x}): "))

for x in phone_reg:
    valid_number(x)
