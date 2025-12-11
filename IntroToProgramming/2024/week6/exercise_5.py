MAX_LINE = 5
line = 0
for x in reversed(range(10, 51, 2)):
    if line == MAX_LINE:
        line = 0
        print('')
    print(x, " ", end='')
    line += 1
print()
