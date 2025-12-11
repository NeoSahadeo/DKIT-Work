cycling = int(input("Hours Cycling: "))
jogging = int(input("Hours Jogging: "))
swimming = int(input("Hours Swimming: "))

calories_burnt = 200 * cycling + 475 * jogging + 275 * swimming

print(f"Weight lost: {calories_burnt / 3500}")
