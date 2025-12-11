def print_dict(my_dict):
    print('-' * 20)
    """
        Retrieve all items (key-value pairs) for the dictionary,
        sotring the key in k and the value in  v

        items() retuns a tuple, so we need to specify that wer're extracting from a tuple
        in our arugment inpacking, i.e. (k, v)
    """

    for x, (y, z) in enumerate(my_dict.items()):
        print(f"{x}) Key: {y} -> Value: {z}")
    print("-" * 20)

if __name__ == "__main__":

    dns = {
        "localhost": "127.0.0.0",
        "google.com": "196.23.12.8",
        "moodle.dkit.ie": "234.122.35.1",
        "dkit.ie": "234.122.44.12",
    }

    print_dict(dns)

    dns["moodle.dkit.ie"] = None

    dkit_routes = {}

    for k, v in dns.items():
        if v is not None and v[0:7] == "234.122":
            dkit_routes[k] = v


    print_dict(dkit_routes)
    minimum = min(dns)
    print(minimum)
    print(dns)
    dns.pop("localhost")
    length = len(dns)
    print("The length of the DNS dictionary is: {length}")
    value = dns.pop("local", None)
    print(value)
