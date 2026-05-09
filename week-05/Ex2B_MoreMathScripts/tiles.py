import math

length = float(input("Enter the room length in feet: "))
width = float(input("Enter the room width in feet: "))

area = length * width

total_tiles = area * 1.10

boxes = math.ceil(total_tiles / 12)

print(f"You need to buy {boxes} boxes of tiles.")