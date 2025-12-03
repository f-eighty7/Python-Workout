from random import randint


def guessing_game():
    """
    Runs a CLI number guessing game where the user has limited attempts
    to guess a random integer between 1 and 100.

    The game loop handles input validation, tracks remaining chances,
    and provides feedback on whether guesses are too high or too low.
    """
    chances = 3
    target_number = randint(1, 100)

    while True:
        # Logic: Check for game over condition at the very start of the loop.
        # This acts as a 'gatekeeper' to prevent the input() function below
        # from triggering a 4th time after the 3rd wrong guess.
        if chances == 0:
            print(
                f"You have lost all your chances. The answer was: {target_number}. Goodbye!"
            )
            break

        user_input = input(
            f"Guess the number between 1-100 (You have {chances} chances left): "
        )

        try:
            user_guess = int(user_input)
        except ValueError:
            print(
                f"\nInput '{user_input}' is invalid; please enter a numeric value between 1-100.\n"
            )
            continue

        if user_guess < 1 or user_guess > 100:
            print("\nThe number must be between 1-100\n")
            continue

        if user_guess == target_number:
            print(f"\nYou have guessed correctly! The answer is: {target_number}")
            break

        if user_guess > target_number:
            print("\nToo high! Try again\n")
        else:
            print("\nToo low! Try again\n")

        chances -= 1


guessing_game()
