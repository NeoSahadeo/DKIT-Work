from email_func import validate_email


if __name__ == '__main__':

    # Create the email information
    subject = input('Subject: ')

    while True:
        recipient = input('Recipient email: ').strip()
        if validate_email(recipient):
            break
        else:
            print('Email is not valid!')

    message = input('Message: ')

    # Store information
    email_data = []
    email_data.append(f'{subject}%%')
    email_data.append(f'{recipient}%%')
    email_data.append(f'{message}\n')


    # Write email information to file
    with open('email.txt', 'a') as file_handler:
        file_handler.writelines(email_data)
