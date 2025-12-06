from decimal import Decimal


def run_timing():
    """
    Continually prompts the user for run times and calculates the average.
    Exits loop upon receiving an empty string.
    """
    total_runs = 0
    total_time = 0

    while True:
        user_input = input("Enter 10 km run time (Press Enter to calculate): ")

        if not user_input:
            break

        try:
            time = float(user_input)
        except ValueError:
            print("Hey! That's not a valid number!")
            continue

        total_runs += 1
        total_time += time

    if total_runs > 0:
        average_time = total_time / total_runs
        print(f"Average of {average_time:.2f}, over {total_runs} runs")
    else:
        print("No runs were entered")


run_timing()


def before_and_after_float(number, before=0, after=0):
    """
    Reconstructs a float by slicing specific digits before and after the decimal.

    Note: This assumes the input 'number' contains a decimal point.
    """
    s = str(number).split(".")

    # Slices the end of the integer part and the start of the fractional part
    output = ".".join([s[0][-before:], s[1][:after]])
    return float(output)


print(before_and_after_float(12345.678, 2, 3))


def sumdecimal(a, b):
    """
    Adds two numbers using the Decimal class to avoid floating-point artifacts.
    """
    print(Decimal(a) + Decimal(b))


sumdecimal("0.1", "0.2")
