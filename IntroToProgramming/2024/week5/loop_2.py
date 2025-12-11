height = 10
size = 1

for x in range(height):
    p = (height - (int(height/2)+size)) * " "
    print(height - (int(height/2)+size))
    print(p, end="")
    for y in range(size):
        print("*", end="")
    print(" ")
    size += 1
