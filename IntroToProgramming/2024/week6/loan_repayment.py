MONTHLY_PAYMENT = 500

# Interest per month
INTEREST_PERCENT = (0.003333333333)  # This is 4% yearly

LOAN = 10_000
MONTHS = 0


while True:
    LOAN += LOAN * INTEREST_PERCENT #  Increase loan
    LOAN -= MONTHLY_PAYMENT #  Subtract the payment
    MONTHS += 1  # Increase months

    # If loan is fully payed back - which it might
    # be less than zero - we end the loop
    if LOAN <= 0:
        print(MONTHS)
        break