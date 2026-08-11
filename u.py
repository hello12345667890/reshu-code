
import random


def number_guessing_game():
    secret_number = random.randint(1, 50)
    max_attempts = 5
    attempts_left = max_attempts

    print("Welcome to the Number Guessing Game!")
    print("I have picked a secret number between 1 and 50.")
    print(f"Lives: {'❤️ ' * attempts_left}\n")

    while attempts_left > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < 1 or guess > 50:
            print("Your guess must be between 1 and 50.")
            continue

        if guess == secret_number:
            print(
                f"\n🎉 Congratulations! You guessed the secret number ({secret_number}) correctly!"
            )
            break

        attempts_left -= 1

        # Provide a hint based on how far off the guess is
        difference = abs(secret_number - guess)
        if difference <= 3:
            hint = "Extremely hot!"
        elif difference <= 7:
            hint = "Very warm!"
        elif difference <= 15:
            hint = "Cold."
        else:
            hint = "Freezing cold!"

        # Indicate direction (higher or lower)
        direction = "Too low" if guess < secret_number else "Too high"

        print(f"Wrong guess! Hint: {direction} ({hint})")
        print(f"Remaining Lives: {'❤️ ' * attempts_left}\n")

    if attempts_left == 0:
        print(f"❌ Game over! The secret number was {secret_number}.")


if __name__ == "__main__":
    number_guessing_game()
