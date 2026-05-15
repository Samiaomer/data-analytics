
# ── Function 1 ──────────────────────────────────────────────────────────────
def display_mailing_label(name, address, city, state, zip):
    """Display data formatted as a mailing address label."""
    print("┌─────────────────────────────────┐")
    print(f"  {name}")
    print(f"  {address}")
    print(f"  {city}, {state}  {zip}")
    print("└─────────────────────────────────┘")
    print()


# ── Function 2 ──────────────────────────────────────────────────────────────
def add_numbers(*args):
    """Accept any number of integer arguments, sum them, and display the equation."""
    result = sum(args)
    equation = " + ".join(str(n) for n in args)
    print(f"{equation} = {result}")


# ── Function 3 ──────────────────────────────────────────────────────────────
def display_receipt(total_due, amount_paid):
    """Display a receipt showing total due, amount paid, and change or balance."""
    print(f"  Total Due:    ${total_due:.2f}")
    print(f"  Amount Paid:  ${amount_paid:.2f}")

    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"  Change Due:   ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"  Remaining balance to be paid: ${balance:.2f}")
    print()


# ── Calls ────────────────────────────────────────────────────────────────────

# a) display_mailing_label() — two different people
display_mailing_label("Menal Omer", "123 Maple Street", "Springfield", "VA", "22302")
display_mailing_label("Hashim Omer", "4587 Ocean Drive", "Annandale", "VA", "22304")

# b) add_numbers() — one number, two numbers, more than two
add_numbers(7)
add_numbers(14, 26)
add_numbers(3, 8, 15, 22, 41)

print()

# c) display_receipt() — overpay, exact, underpay
display_receipt(45.75, 60.00)   # overpay
display_receipt(32.50, 32.50)   # exact
display_receipt(78.99, 50.00)   # underpay