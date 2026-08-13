name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")

basic_salary = float(input("Enter basic salary: "))
working_days = int(input("Enter working days: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate: "))
tax_percent = float(input("Enter tax percentage: "))

# Calculate overtime pay
overtime_pay = overtime_hours * overtime_rate

# Calculate gross salary
gross_salary = basic_salary + overtime_pay

# Calculate tax
tax = gross_salary * tax_percent / 100

# Calculate net salary
net_salary = gross_salary - tax

print("\n--------- PAYSLIP ---------")
print("Name:", name)
print("Employee ID:", employee_id)
print("Working Days:", working_days)
print("Basic Salary:", basic_salary)
print("Overtime Pay:", overtime_pay)
print("Gross Salary:", gross_salary)
print("Tax:", tax)
print("Net Salary:", net_salary)