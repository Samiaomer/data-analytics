# Variables
pay_rate = 17.30
hours_worked = 45

# Calculate gross pay
if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = pay_rate * hours_worked

# Print result
print("Pay Rate:", pay_rate)
print("Hours Worked:", hours_worked)
print("Gross Pay:", gross_pay)