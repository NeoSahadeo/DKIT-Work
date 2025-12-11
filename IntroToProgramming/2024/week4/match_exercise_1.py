traffic_light_color = input("What color is the traffic light?: \n").lower()

match traffic_light_color:
    case "green":
        print("GO!")
    case "yellow":
        print("CAUTION!")
    case "red":
        print("STOP!")
    case _:
        print("Invalid color")
