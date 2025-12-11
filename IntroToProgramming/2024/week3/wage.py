# Exercise C5

# Wage = 12.70
# 40 <= Regular pay
# 40 > x > 50 = 1.5 times pay
# 50 > = 2 times pay

WAGE = 12.70
hours_worked = int(input("Please enter the amount of hours worked: "))
wage = 0  # no money to start

# # regular pay
if hours_worked <= 40:
    # Regular pay
    wage = hours_worked * WAGE

# 1.5 times pay after 40 hours
elif hours_worked > 40 and hours_worked <= 50:
    overtime_pay = hours_worked - 40

    # Regular pay + 1.5 pay
    wage = 40 * WAGE + overtime_pay * (1.5 * WAGE)

else:
    overtime_pay = hours_worked - 50

    # Regular pay + 1.5 pay + 2 pay
    wage = 40 * WAGE + 10 * (1.5 * WAGE) + overtime_pay * (2 * WAGE)

print(f"Gross wage: {wage:.2f}")
