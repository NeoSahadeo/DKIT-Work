amount_spent = int(input("How much did you spend: "))
discount_percent = 0

if amount_spent > 100:
    discount_percent = 20
elif amount_spent > 50:
    discount_percent = 10

dicounted = amount_spent * (discount_percent / 100)

print(f"Dicount: {dicounted:.2f}")
