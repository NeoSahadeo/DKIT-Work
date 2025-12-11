from exA2_fun import generate_password


if __name__ == '__main__':
    passwords = generate_password(int(input("How many password do you want to generate?: ")))
    for x in passwords:
        print(x)
