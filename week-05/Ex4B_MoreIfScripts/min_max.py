# Variables
a = 10
b = 25
c = 7

# Find the smallest number
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Find the largest number
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Print results
print("The smallest number is:", smallest)
print("The largest number is:", largest)