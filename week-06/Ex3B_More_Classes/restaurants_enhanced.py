class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"\n{self.restaurant_name.title()} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name.title()} is now open!")

    def add_num_served(self):
        """Prompt for number of customers served today and add to total."""
        served_today = input("How many customers served today? ")
        self.number_served += int(served_today)

    def print_num_served(self):
        """Print the total number of customers served."""
        print(f"{self.restaurant_name.title()} has served {self.number_served} customers.")

    def customer_rating(self):
        """
        Prompt for a rating of 1-5 and add to ratings list.
        Handles invalid input (non-integers, out-of-range values) with a loop.
        """
        while True:
            raw = input(
                "How would you rate your experience today on a scale of 1-5 "
                "(5 being excellent)? "
            )

            # Check that the input is a whole-number string before converting
            if not raw.strip().lstrip('-').isdigit():
                print("Invalid input. Please enter a whole number between 1 and 5.")
                continue

            rating = int(raw.strip())

            if rating < 1 or rating > 5:
                print("Invalid input. Please enter a whole number between 1 and 5.")
                continue

            # Valid rating — record and report
            self.customer_ratings.append(rating)
            avg = sum(self.customer_ratings) / len(self.customer_ratings)
            print(
                f"Your rating was {rating}. "
                f"The average rating for {self.restaurant_name.title()} is {avg:.1f}."
            )
            break


# ── Test instances ──────────────────────────────────────────────────────────

restaurant_1 = Restaurant("east west", "turkish")
restaurant_2 = Restaurant("bawadi", "middle eastern")
restaurant_3 = Restaurant("kolbeh", "turkish")

restaurants = [restaurant_1, restaurant_2, restaurant_3]

# ── Part a: print_num_served / add_num_served ───────────────────────────────

print("\n=== Part a: Customers Served ===")

for r in restaurants:
    r.describe_restaurant()

    # Check initial value (should be 0)
    r.print_num_served()

    # Add customers a few times
    r.add_num_served()
    r.add_num_served()
    r.add_num_served()

    # Check updated total
    r.print_num_served()

# ── Part b & c: customer_rating (with validation) ──────────────────────────

print("\n=== Part b & c: Customer Ratings ===")

for r in restaurants:
    r.describe_restaurant()
    # Run several rating prompts per restaurant
    for _ in range(3):
        r.customer_rating()