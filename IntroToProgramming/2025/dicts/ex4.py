radiation = {
    "a": "Alpa",
    "b": "Beta",
    "g": "Gamma",
    "x": "XRay",
}

radiation["c"] = "Cherenkov"
radiation["x"] = "UltraViolet"

x = input("Please enter new radiation entry: ")
if x not in radiation:
    rad = input("Enter radiation name: ")
    radiation[x] = rad
    print(radiation)
else:
    print("Radiation symbol exists!")
