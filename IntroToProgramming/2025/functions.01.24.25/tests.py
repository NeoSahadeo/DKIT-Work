import unittest
from exA2 import generate_password
from exB3 import generate_username
from exC5 import validate


class Tests(unittest.TestCase):
    def test_exA2(self):
        passwords = generate_password(10)
        print(passwords)

    def test_exB3(self):
        generate_username('Neo', 'Sahadeo')
        generate_username('Neo', 'Saha')
        generate_username('Neo', 'Sahad')
        generate_username('Neo', 'Sahade')

    def test_exC5(self):
        result = validate("1Password@12")
        if result:
            print("Password is valid")
        else:
            print("Password is invalid")


if __name__ == '__main__':
    unittest.main()
