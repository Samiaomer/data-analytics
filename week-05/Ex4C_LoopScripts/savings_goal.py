# savings_goal.py

# Starting values
bank_balance = 100
savings_goal = 500
weekly_savings = 50

# While loop
while bank_balance < savings_goal:
    bank_balance += weekly_savings
    print(f"This week my balance increased to {bank_balance}.")

# Final message
print(f"Goal met! My current balance is {bank_balance}.")

# savings_goal.py

# Starting values
bank_balance = 100
savings_goal = 500
weekly_savings = 50

# While loop
while bank_balance < savings_goal:
    bank_balance += weekly_savings

    # 75% or more of goal
    if bank_balance >= savings_goal * 0.75:
        bank_balance -= 20  # Treat yourself
        print(f"So close! After treating myself, my balance is up to {bank_balance}.")

    # More than halfway to goal
    elif bank_balance > savings_goal / 2:
        print(f"Almost there! This week my balance is up to {bank_balance}.")

    # Regular message
    else:
        print(f"This week my balance increased to {bank_balance}.")

# Final message
print(f"Goal met! My current balance is {bank_balance}.")

