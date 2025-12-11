# CONTANTS
BPS = [500, 2000, 100_000]
NORMAL_POINTS = [500, 1500, 98_000]  # Normal points should be the diff between values and equal in length to BPS
RATES = [0.01, 0.02, 0.03, 0.05]  # Rates should be 1 more than BPS
BPS_LEN = len(BPS)


def cal_interest(principle):
    if principle <= 0:
        return 0
    points = []

    # Spread values about BPS
    for index, value in enumerate(BPS):
        result = principle - value
        prev = principle - BPS[index - 1]
        if result > 0:
            points.append(value)
        elif prev > 0:
            points.append(prev)
            break
        else:
            points.append(principle)
            break

        if result > 0 and index == len(BPS) - 1:
            points.append(result)

    # Normalise values
    for index, value in enumerate(points):
        if index < BPS_LEN and points[index] == BPS[index]:
            points[index] = NORMAL_POINTS[index]

    # Calculate interest
    interest = 0
    for index, value in enumerate(points):
        interest += RATES[index] * value

    return round(interest, 2)


if __name__ == "__main__":
    print(cal_interest(1_000_000))
