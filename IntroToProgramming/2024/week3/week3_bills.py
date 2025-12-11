TIP_PERCENTAGE = 0.1
MINIMUM_TIP = 4


def calc_tip(bill_total):
    if type(bill_total) != float:
        raise Exception("Value is not a float")

    tip = bill_total * TIP_PERCENTAGE

    if tip < MINIMUM_TIP:
        print(f"Tip was: {tip}, minimum tip is {MINIMUM_TIP}.")
        tip = MINIMUM_TIP

    return bill_total + tip


if __name__ == '__main__':
    print(calc_tip(float(input("Enter bill total: "))))


# bill = float(input("How much is the bill: "))
# ----->
