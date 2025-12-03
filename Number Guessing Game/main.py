from random import randint


def guessing_game():
    target_number = randint(1, 100)

    while True:
        user_input = input("Guess the number between 1-100: ")

        try:
            user_guess = int(user_input)
        except ValueError:
            print(
                f"\nInput '{user_input}' is invalid; please enter a numeric value between 1-100.\n"
            )
            continue

        if user_guess == target_number:
            print(f"\nYou have guessed correctly! The answer is: {target_number}")
            break

        if user_guess > target_number:
            print("\nToo high! Try again\n")
        else:
            print("\nToo low! Try again\n")


guessing_game()
