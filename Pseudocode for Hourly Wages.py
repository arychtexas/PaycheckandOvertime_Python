# Input data for calculations
Your_name = input("What is your name?: ")
hours_worked = int(input("Enter the number of hours worked: "))
hourly_rate = int(input("Enter the hourly rate. This rate is a dollar amount e.g. 40. DO NOT USE special characters.: "))
overtime_rate = int(input("Enter the overtime rate. This rate is a dollar amount e.g. 40. DO NOT USE special characters.: "))
standard_hours = 40


# Paycheck calculation
if hours_worked <= standard_hours:
    paycheck = hours_worked * hourly_rate
else:
    regular_pay = standard_hours * hourly_rate
    overtime_hours = hours_worked - standard_hours
    overtime_pay = overtime_hours * overtime_rate
    paycheck = regular_pay + overtime_pay

# Output the result
print(f"{Your_name}'s paycheck for {hours_worked} hours worked is ${paycheck:.2f}")
