emp_sal = []

while True:
    employee_name = input("Enter the employee name (or enter 'stop'): ")
    if employee_name == 'stop':
        break

    employee_salary = float(input("Enter the employee salary: "))

    emp_sal.append([employee_name, employee_salary])


print('__Roster__')
for x in range(0, len(emp_sal)):
    print(f"{emp_sal[x][0]}:{emp_sal[x][1]}\t:Pos->{x}")
