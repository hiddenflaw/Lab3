employee_salaries = {}

while True:
    name = input("Enter employee name: ")
    if name.lower() == 'no':
        break
    salary = float(input("Enter employee salary: "))
    employee_salaries[name] = salary

print("\nEmployee salaries recorded:")
for name, salary in employee_salaries.items():
    print(f"{name}: ${salary}")