# Neo Sahadeo 16/10/2024

# Constants:
RATE_MEMBER = 5  # 5 euro per hour for members
RATE_NON_MEMBER = 10  # 10 euro per hour for non-members
TAX_MEMBERS = 0.1  # 10% tax for members
TAX_NON_MEMBERS = 0.2  # 20% tax for non-members

# Get the time the user has used the service for.
hours_used = float(input("Hours service was used for: "))

# Check if the user is member of the scheme.
# Added [0] to get the first letter and
# added .lower() to clean data.
is_memeber = input("Are you currently a member? (y/n): ")[0].lower()

# Service bill is the amount the user has to pay.
# Set to -1 by default to make it clear if an
# error occurs.
service_bill = -1

# Boolean logic to check if the user input
# is equal to "y" or "n"
if is_memeber == "y":
    # Hours for service used
    hours_billed = (hours_used * RATE_MEMBER)
    # Service bill total
    service_bill = hours_billed + hours_billed * TAX_MEMBERS

elif is_memeber == "n":
    # Hours for service used
    hours_billed = (hours_used * RATE_NON_MEMBER)
    # Service bill total
    service_bill = hours_billed + hours_billed * TAX_NON_MEMBERS

# Display the total cost
print(f"Total Service Bill: {service_bill}")
