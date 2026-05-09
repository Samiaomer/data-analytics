# Create a list of movies
movies = ["Layl", "Crystal", "Salma"]

# Use len() to print the descriptive statement
print("The list movies includes my top", len(movies), "favorite movies")

# Print the complete list
print(movies)

# Create a list of movies (NOT in alphabetical order)
movies = ["Salma", "Layl", "Crystal"]

# a) Using sorted() - does NOT change original list
print("Sorted using sorted():", sorted(movies))
print("Original list after sorted():", movies)

# What you notice:
# sorted() shows an alphabetical version BUT does NOT change the original list

print()

# b) Using .sort() - permanently changes the list
movies.sort()
print("List after .sort():", movies)

# What you notice:
# .sort() changes the original list permanently into alphabetical order

print()

# 5. Add one more movie using append()
movies.append("Amira")

# Print updated list and description
print(f"Updated list includes my top {len(movies)} favorite movies")
print(movies)