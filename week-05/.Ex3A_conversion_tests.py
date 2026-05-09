# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

# Define variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# -------------------------
# Variable a conversions
# -------------------------
a_float = float(a)
print(a_float)

# -------------------------
# Variable b conversions
# -------------------------
b_int = int(b)
b_float = float(b)

print(b_int)
print(b_float)

# -------------------------
# Variable c conversions
# -------------------------
# c_int = int(c)      # ValueError: invalid literal for int()
# c_float = float(c)  # ValueError: could not convert string to float

# -------------------------
# Variable d conversions
# -------------------------
# d_int = int(d)      # ValueError: invalid literal for int()
# d_float = float(d)  # ValueError: could not convert string to float

print(a_float, type(a_float))
print(b_int, type(b_int))
print(b_float, type(b_float))
print(c, type(c))
print(d, type(d))

# ======================================================
# PART 2: TYPE CASTING + STRING MANIPULATION TESTS
# ======================================================

# -------------------------
# Variable a = " 101.1 "
# -------------------------

# a) Cast as integer
# int(a)  # ERROR: ValueError (cannot convert string with decimal to int directly)

# b) Cast as float
a_float = float(a.strip())   # SUCCESS: converts to 101.1

# c) float then int
a_int_from_float = int(float(a.strip()))  # SUCCESS: 101 (decimal removed)

# d) slicing numeric portion + convert
a_slice = a.strip()[0:5]  # "101.1"
a_slice_float = float(a_slice)  # SUCCESS: 101.1
a_slice_int = int(float(a_slice))  # SUCCESS: 101

# e) strip() in print
print(a.strip(), type(a.strip()))  # "101.1" as string after stripping spaces


# -------------------------
# Variable b = '55'
# -------------------------

# a) int
b_int = int(b)  # SUCCESS: 55

# b) float
b_float = float(b)  # SUCCESS: 55.0


# -------------------------
# Variable c = "402 Stevens"
# -------------------------

# a) int
# int(c)  # ERROR: ValueError (contains letters)

# b) float
# float(c)  # ERROR: ValueError

# d) slicing numeric portion
c_slice = c[0:3]  # "402"
c_int = int(c_slice)  # SUCCESS: 402

# e) strip in print
print(c.strip(), type(c.strip()))  # still string "402 Stevens"


# -------------------------
# Variable d = 'Number 5 '
# -------------------------

# a) int
# int(d)  # ERROR: ValueError

# b) float
# float(d)  # ERROR: ValueError

# d) slicing numeric portion
d_slice = d[-2]  # "5"
d_int = int(d_slice)  # SUCCESS: 5

# e) strip in print
print(d.strip(), type(d.strip()))  # "Number 5"