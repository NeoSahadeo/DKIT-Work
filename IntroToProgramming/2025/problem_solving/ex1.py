def find_high(numbers):
    highest = numbers[0]
    for x in numbers:
        if x > highest:
           highest = x
    return highest

print(find_high([6,3,1,3,8,10,3,11]))
print(find_high([-3,-6,-1,-10,-20,-30]))
