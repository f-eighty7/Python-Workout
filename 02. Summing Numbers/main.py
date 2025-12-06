def mysum(*numbers, start=0):
    """
    Calculates the sum of a variable number of arguments.

    Args:
        *numbers: Variable length argument list of numbers.
        start (int, optional): The value to start the sum from. Defaults to 0.

    Returns:
        int/float: The total sum.
    """
    output = start
    for number in numbers:
        output += number
    return output


print(mysum(*[10, 20, 30, 40], start=5))


def myavg(numbers):
    """
    Calculates the arithmetic mean of a list of numbers.

    Returns:
        float: The average value.
    """
    output = 0
    for number in numbers:
        output += number

    # Returns float; division by zero will occur if list is empty
    return output / len(numbers)


print(myavg([5, 19, 3, 10]))


def get_word_stats(words):
    """
    Analyzes a list of strings to find length statistics.

    Returns:
        tuple: (shortest_length, longest_length, average_length)
    """
    # Initialize min/max using the first element to avoid importing infinity
    # or using arbitrary magic numbers. Assumes list is not empty.
    shortest = len(words[0])
    longest = len(words[0])
    total_len = 0

    for word in words:
        current_len = len(word)
        total_len += current_len

        if current_len < shortest:
            shortest = current_len

        if current_len > longest:
            longest = current_len

    avg = total_len / len(words)

    return (shortest, longest, avg)


print(get_word_stats(["howmanywordsami", "amishort"]))


def sum_only_numbers(objects):
    """
    Sums a mixed list, including integers and strings that contain only digits.
    Ignores other types, floats, or mixed alphanumeric strings.
    """
    mysum = 0

    for number in objects:
        if isinstance(number, int):
            mysum += number
        elif isinstance(number, str) and number.isdigit():
            converted_number = int(number)
            mysum += converted_number
        else:
            pass
    return mysum


print(sum_only_numbers([1, 100, "5", "five"]))
