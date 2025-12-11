http_code = int(input("Enter the status code: "))

match http_code:
    case 200:
        print("OK")
    case 301:
        print("Permanent Redirect")
    case 307:
        print("Temporary Redirect")
    case 404:
        print("Not Found")
    case 410:
        print("Gone")
    case 500:
        print("Internal Server Error")
    case 503:
        print("Service Unavailable")
    case _:
        print("Code is invalid")
