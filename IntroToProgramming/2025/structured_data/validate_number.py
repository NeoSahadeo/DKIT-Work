def validate(phone_num):
    """
    Validate the the phone number
    """
    return (len(phone_num) == 10 and
            phone_num.isdigit() and
            phone_num[0:3] in ["083", "085", "086", "087", "088"])
