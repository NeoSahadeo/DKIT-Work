import random

SPECIAL_CHARS = ["!", "@", "#", "$", "%", "^", "&", "*", ";", ".", ",", "?", ]

TOKENS = {"lowercase": 3,
          "uppercase": 1,
          "special_characters": 2,
          "digits": 2}


def generate_password(amount):
    password_arr = []
    for _ in range(0, amount):
        password = []
        for _, token_name in enumerate(TOKENS):
            for x in range(0, TOKENS[token_name]):
                character = None
                if token_name == 'lowercase':
                    character = chr(random.randint(97, 122))
                elif token_name == 'uppercase':
                    character = chr(random.randint(65, 91))
                elif token_name == 'digits':
                    character = chr(random.randint(65, 91))
                elif token_name == 'special_characters':
                    character = SPECIAL_CHARS[random.randint(0, len(SPECIAL_CHARS) - 1)]
                password.append(str(character))

        password_length = len(password) - 1
        for index, value in enumerate(password):
            # My implementation of a fisher-yates algo
            current_length = password_length - index
            position = random.randint(0, current_length)
            prev = password[current_length]
            next = password[position]
            password[current_length] = next
            password[position] = prev

        password_arr.append(''.join(password))
    return password_arr
