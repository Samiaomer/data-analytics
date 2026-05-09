# Assets
cash = 2000
car_value = 5000
savings = 3000

# Debts
credit_card = 1000
loan = 2500

# Calculate totals
total_assets = cash + car_value + savings
total_debts = credit_card + loan

# Calculate net worth
net_worth = total_assets - total_debts

# Output
print("Your total assets are", total_assets)
print("Your total debts are", total_debts)
print("Your net worth is", net_worth)

# Rectangle sides based on birthday
side_a = 3
side_b = 15

# Calculate area
area = side_a * side_b

# Output
print("Side A is", side_a)
print("Side B is", side_b)
print("The area of the rectangle is", area)

# Restaurant bill
bill_total = 50

# Tip percentage
tip_percentage = 0.20

# Calculate tip
tip_amount = bill_total * tip_percentage

# Output
print("The tip on a $" + str(bill_total) + " restaurant bill is $" + str(tip_amount))

# Diameter based on birthday day
diameter = 15

# Calculate radius
radius = diameter / 2

# Calculate area
area = 3.14 * radius * radius

# Output
print("The area of a circle with radius", radius, "is", area)

# Savings amount
savings = 1000

# Interest rate
interest_rate = 0.06

# Calculate doubled savings
doubled_savings = savings * 2

# Rule of 72 calculation
years = 72 / 6

# Output
print("Your current savings is", savings)

print(
    "At a",
    format(interest_rate, ".0%"),
    "interest rate, your savings account will be worth",
    format(doubled_savings, ".2f"),
    "in",
    format(years, ".1f"),
    "years"
)


# Ask user for input values
bank_bal = input("What is your current bank balance? ")
interest_rate = input("What is the interest rate (in %)? ")

# Convert inputs from string to numbers
bank_bal = float(bank_bal)
interest_rate = float(interest_rate)

# Simple calculation (example: interest earned)
interest_earned = bank_bal * (interest_rate / 100)

# Output results
print("Your bank balance is:", bank_bal)
print("Your interest earned is:", interest_earned)
# Observations / Pitfalls of using input():
# 1. input() always returns a STRING, so math will not work unless we convert it to int or float.
# 2. If the user types letters instead of numbers, the program will crash (ValueError).
# 3. Users can enter unexpected values (empty input, negative numbers, etc.).
# 4. input() makes programs interactive but harder to automate testing.
# 5. Extra spaces or wrong formatting can also cause errors when converting data types.

# Ask user for input values
bank_bal = input("What is your current bank balance? ")
interest_rate = input("What is the interest rate (in %)? ")

# Convert inputs from string to numbers
bank_bal = float(bank_bal)
interest_rate = float(interest_rate)

# Simple calculation
interest_earned = bank_bal * (interest_rate / 100)

# Output results using f-strings
print(f"Your bank balance is: ${bank_bal}")
print(f"Your interest earned is: ${interest_earned}")
# f-strings make printing easier and cleaner
# They allow variables to be placed directly inside {} without using + or str()
# Example: f"Your balance is {bank_bal}" instead of "Your balance is " + str(bank_bal)