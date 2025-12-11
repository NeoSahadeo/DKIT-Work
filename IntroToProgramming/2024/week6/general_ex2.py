breakpoint = 0
total = 0
for x in range(3, 24):
    total += x
    if total > 200:
        breakpoint = x
        break

print(x)
