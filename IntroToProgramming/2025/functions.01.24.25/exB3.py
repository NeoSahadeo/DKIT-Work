from exB3_fun import generate_username

if __name__ == "__main__":
    firstname = input("Firstname: ").strip()
    lastname = input("Lastname: ").strip()
    generate_username(firstname, lastname)
