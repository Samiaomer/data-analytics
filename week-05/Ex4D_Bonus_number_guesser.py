# Number Guessing Game

# Create a pool of numbers
numbers = list(range(1, 21))

# Shuffle the numbers without using random module
shuffled_numbers = []

while numbers:
    index = len(numbers) // 2
    shuffled_numbers.append(numbers.pop(index))

# Pick the secret number
secret_number = shuffled_numbers[0]

print("Guess the secret number between 1 and 20!")

# Variables for bonus features
guess_count = 0
guessed_numbers = []

while True:
    guess = input("Enter your guess: ")

    # Safe for non-numeric input
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    # Track guesses
    guess_count += 1
    guessed_numbers.append(guess)

    if guess < secret_number:
        print("Higher!")
    elif guess > secret_number:
        print("Lower!")
    else:
        print("Correct! You guessed the number!")

        print(f"Total guesses: {guess_count}")
        print(f"Your guesses: {guessed_numbers}")

        if guess_count < 5:
            print("Awesome guessing skills!")

        break