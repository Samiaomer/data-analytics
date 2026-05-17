class Restaurant:
    '''Represents a restaurant with a name and type of food served.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


# Three instances of Restaurant
restaurant_1 = Restaurant("Bella Italia", "Italian food")
restaurant_2 = Restaurant("Sushi Palace", "Japanese food")
restaurant_3 = Restaurant("Taco Loco", "Mexican food")

# Call both methods for each instance
restaurant_1.describe_rest()
restaurant_1.rest_open()

restaurant_2.describe_rest()
restaurant_2.rest_open()

restaurant_3.describe_rest()
restaurant_3.rest_open()