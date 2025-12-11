# Neo Sahadeo 16/10/2024

# Constants:
TAX_RATE = 0.42  # This is tax rate for the user.

# Get the salary hourly rate.
salary_per_hour = float(input("Salary hourly rate: "))

# Get the number of hours worked in the last month.
# I am using float because it will eventually be converted
# to a type of float.
number_of_hours_worked = float(input("Hours worked in the last month: "))

# Gross pay is the total pay before any deductions.
# f(x) = sh
gross_pay = salary_per_hour * number_of_hours_worked

# Calculate the tax cost
# f(x) = xR
tax_due = gross_pay * TAX_RATE

# Calculate net pay
# f(x) = g - t
net_pay = gross_pay - tax_due

# Display everything
print(f"""
Gross Pay: \t {gross_pay:.2f}
Tax Due: \t {tax_due:.2f}
Net Pay: \t {net_pay:.2f}
""")
