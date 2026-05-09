import math

people = int(input("Enter number of tourists: "))

# Calculate vans needed
vans = math.ceil(people / 15)

# Calculate total cost
total_cost = vans * 250

# Cost per person
cost_per_person = total_cost / people

print(f"Number of vans needed: {vans}")
print(f"Total rental cost: ${total_cost}")
print(f"Cost per person: ${cost_per_person:.2f}")