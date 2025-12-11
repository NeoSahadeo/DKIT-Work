radiation = {
    "a": "Alpa",
    "b": "Beta",
    "g": "Gamma",
    "x": "XRay",
}

keys = radiation.keys()
print(keys)

for index, value in enumerate(keys):
    print(index, value, radiation[value])


values = radiation.values()
print(values)

for index, value in enumerate(values):
    print(index, value)
