# 1 & 2. Create two tuples
candy_types = ("Skittles", "Starburst", "Jelly Beans")
fruit_flavors = ("Strawberry", "Mango", "Orange")

# 3. Create a set for candy combinations
candy_combinations = set()

# Add combinations using tuple indexing
candy_combinations.add((candy_types[0], fruit_flavors[1]))
candy_combinations.add((candy_types[1], fruit_flavors[0]))
candy_combinations.add((candy_types[2], fruit_flavors[2]))

# 4. Print message and set
print("Today's candy options include:")
print(candy_combinations)

# 5. Print multiple times to see order behavior
print(candy_combinations)
print(candy_combinations)