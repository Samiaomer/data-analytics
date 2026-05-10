# List of favorite foods
foods = ["tacos", "ramen", "jerk chicken", "injera", "pierogi"]

# Print numbered list
for index, food in enumerate(foods, start=1):
    if index == 1:
        print(f"{index}. {food} <- top pick!")
    else:
        print(f"{index}. {food}")

print("\nReverse order:\n")

# Print reversed list
for index, food in enumerate(reversed(foods), start=1):
    print(f"{index}. {food}")