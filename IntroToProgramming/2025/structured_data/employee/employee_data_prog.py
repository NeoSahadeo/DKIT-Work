# Write a program that takes in the name of a file of employee data from the user, then reads in the
# file data and stores it in three lists (names, salaries, job titles). The file data will be structured as:
# Employee name%%salary%%job title

names = []
salaries = []
jobs = []

file_name = input('Filename: ')

file_handler = open(file_name, 'r')

for x in file_handler:
    employee_data_list = x.strip().split("%%")  # Split gives us a list
    names.append(employee_data_list[0])
    salaries.append(employee_data_list[1])
    jobs.append(employee_data_list[2])


file_handler.close()


# Once this data has been read in and stored appropriately, your program should find the highest
# salary, display it and display all employees paid that salary. It should then find the lowest salary,
# display it and display all job titles paid that salary.


highest_salary = max(salaries)
for x in range(len(salaries)):
    if salaries[x] == highest_salary:
        print(f"{names[x]}: {salaries[x]}")

lowest_salary = min(salaries)
for x in range(len(salaries)):
    if salaries[x] == lowest_salary:
        print(f"{jobs[x]}: {salaries[x]}")
