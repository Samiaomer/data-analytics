import random

products = [
    'Laptop',
    'Monitor',
    'Keyboard',
    'Mouse',
    'Webcam',
    'Headset',
    'Docking Station',
    'USB Hub',
    'Desk Lamp',
    'Surge Protector'
]
print(products)

# a) Product of the Day (random.choice)
product_of_the_day = random.choice(products)
print("Product of the Day:", product_of_the_day)

# b) Usability survey (random.sample - no repeats)
survey_products = random.sample(products, 3)
print("Usability Survey Products:", survey_products)

# c) Shuffle products (in-place change)
random.shuffle(products)
print("Shuffled Product List:", products)

# d) Simulated daily transactions (random.randint)
transactions = random.randint(50, 300)
print("Daily Transaction Count:", transactions)

