# exception_basics.py
# Demonstrating common Python exceptions with try-except-else-finally blocks

# ─────────────────────────────────────────────
# ValueError
# Raised when a function receives an argument of the right type but an inappropriate value
# ─────────────────────────────────────────────

# Example 1: int() can't convert a non-numeric string
try:
    num = int("banana")
except ValueError:
    print("ValueError: Can't convert a non-numeric string to an integer")
else:
    print(num)
finally:
    print("Let's try another one...\n")

# Example 2: math.sqrt() doesn't accept negative numbers
import math
try:
    result = math.sqrt(-9)
except ValueError:
    print("ValueError: math.sqrt() cannot take the square root of a negative number")
else:
    print(result)
finally:
    print("Let's try another one...\n")

# ─────────────────────────────────────────────
# NameError
# Raised when a local or global name is not found (undefined variable)
# ─────────────────────────────────────────────

# Example 1: Referencing a variable that was never defined
try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable")
else:
    print(m)
finally:
    print("Let's try another one...\n")

# Example 2: Calling a function before it is defined
try:
    result = add_numbers(3, 4)
except NameError:
    print("NameError: Called a function that hasn't been defined yet")
else:
    print(result)
finally:
    print("Let's try another one...\n")

# ─────────────────────────────────────────────
# TypeError
# Raised when an operation is applied to an object of the wrong type
# ─────────────────────────────────────────────

# Example 1: Adding a string and an integer
try:
    result = "hello" + 5
except TypeError:
    print("TypeError: Can't concatenate a string and an integer using '+'")
else:
    print(result)
finally:
    print("Let's try another one...\n")

# Example 2: Calling a non-callable object (integer used as a function)
try:
    num = 42
    num()
except TypeError:
    print("TypeError: An integer is not callable — you can't call it like a function")
else:
    print(num)
finally:
    print("Let's try another one...\n")

# ─────────────────────────────────────────────
# SyntaxError
# Raised when the parser encounters a syntactically incorrect statement
# Note: SyntaxError usually prevents the script from running at all,
# so we use compile() or exec() to trigger it at runtime inside a try block
# ─────────────────────────────────────────────

# Example 1: Missing closing parenthesis
try:
    compile("print('hello'", "<string>", "exec")
except SyntaxError:
    print("SyntaxError: Missing closing parenthesis in the expression")
else:
    print("No syntax error found")
finally:
    print("Let's try another one...\n")

# Example 2: Invalid assignment using a keyword as a variable name
try:
    compile("for = 10", "<string>", "exec")
except SyntaxError:
    print("SyntaxError: Can't use a reserved keyword ('for') as a variable name")
else:
    print("No syntax error found")
finally:
    print("Let's try another one...\n")