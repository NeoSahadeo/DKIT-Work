# Write a function that validates an email address. Your function should take in a single parameter –
# the string to be validated as an email address – and should return True if the string is a legitimate
# email address and False otherwise. A string is considered an email address if:
# • It contains an @ with text before it
# • It contains one . with text before and after it
# • The . appears AFTER the @


# neosahadeo@protonmail.com
# d00264604@student.dkit

def validate_email(email):
    at_is_valid = False
    dot_is_valid = False

    before_at = email[email.find('@') - 1]
    at_location = email.find('@')

    if before_at.isalpha() and at_location > 0:
        at_is_valid = True

    dot_location = email.find('.')
    before_dot = email[email.find('.') - 1]

    # Check if its in the length of the email
    after_dot = ''
    if email.find('.') + 1 < len(email):
        after_dot = email[email.find('.') + 1]

    if before_dot.isalpha() and after_dot.isalpha() and dot_location > 2:
        dot_is_valid = True

    if  at_is_valid and dot_is_valid and email.find('.') > email.index('@'):
        return True
    else:
        return False
