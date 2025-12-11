import csv


def question1(x):
    # function to increment a number x by 2
    return x * 2


def question2(a, b, c):
    '''
    returns the maximum number from a, b or c
    Params: variables a, b, c
    Return: the largest onenumber ,-1 if any number is NaN
    '''

    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c
    return -1


def question3(amount):
    # function to calculate interest
    # if amount is greater than 100 then intererst rate is 5%
    # if amount is greater than 1000 then interest rate is 6%
    # otherwise interest rate is 0

    if amount < 100:
        return 0

    elif amount > 100:
        return float("{:.2f}".format(amount * 0.05))

    elif amount > 1000:
        return float("{:.2f}".format(amount * 0.065))

    return 0


def question4(results, team):
    # calculate the number of points a team has from a results array containing
    # team_name, #win, #draw, #lost
    # 3 points for win
    # 1 point for draw
    # 0 point for lost

    noTeams = len(results)
    points = -1
    for result in results:
        if result[0] == team:
            points = int(result[1]) * 3 + int(result[2]) * 1

    return points


def load_results(file_path):
    array = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            array.append(row)
    return array


if __name__ == "__main__":
    results = load_results("results.txt")
    points = question4(results, "team1")
