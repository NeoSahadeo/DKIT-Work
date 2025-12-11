from exC5_fun import validate

if __name__ == "__main__":
    result = validate(input("Password: "))
    if result:
        print("Password is valid")
    else:
        print("Password is invalid")
