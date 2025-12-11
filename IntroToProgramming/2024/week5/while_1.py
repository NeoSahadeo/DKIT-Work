keep_running = True
total = 0
count = 0
while keep_running == True:
    total += int(input(f"Please enter your grade # {count}: "))
    count += 1
    should_continue = input("Would you like to enter another grade? (y/yes to continue): ")[0].lower()
    if not should_continue == 'y':
        keep_running = False
print(f"Average {total/count}")
