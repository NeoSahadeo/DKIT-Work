def devops(number):
    if not number % 15:
        return "DevOps"
    elif not number % 3:
        return "Dev"
    elif not number % 5:
        return "Ops"
    return str(number)
