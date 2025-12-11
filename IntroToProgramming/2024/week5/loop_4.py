lower_bound = int(input("Enter lower range (inclusive): "))
upper_bound = int(input("Enter upper range (inclusive): "))

_sum = 1
for x in range(lower_bound, upper_bound+1):
    _sum *= x

print(f"The product is: {_sum}")
