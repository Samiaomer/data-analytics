# Variables
pay_rate = 17.30
hours_worked = 45
filing_status = "joint"  # Change to "joint" or "single" to test


# Calculate gross pay (weekly)
if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = pay_rate * hours_worked

# Calculate annual gross income (52 weeks in a year)
annual_income = gross_pay * 52

# Determine tax rate based on filing status and annual income
if filing_status == "single":
    if annual_income < 12000:
        tax_rate = 0.05
    elif annual_income < 25000:
        tax_rate = 0.10
    elif annual_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == "joint":
    if annual_income < 12000:
        tax_rate = 0.00
    elif annual_income < 25000:
        tax_rate = 0.06
    elif annual_income < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

# Calculate weekly tax withholding
weekly_tax = gross_pay * tax_rate

# Calculate net pay
net_pay = gross_pay - weekly_tax

# Print results
print("You worked", hours_worked, "hours this period.")
print("Because you earn $" + str(pay_rate) + " per hour, your gross weekly pay is $" + str(round(gross_pay, 2)))
print("Your filing status is", filing_status)
print("Your tax withholding for the week is $" + str(round(weekly_tax, 2)))
print("Your net pay is $" + str(round(net_pay, 2)))