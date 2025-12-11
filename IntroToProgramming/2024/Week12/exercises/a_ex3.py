user_input = int(input("Enter a number for the corres month(1 = Jan, 12 = Dec): "))

months = ["Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec"]

print(months[user_input - 1])
