def firstlast(sequence):
    return sequence[:1] + sequence[-1:]


print(firstlast("abcd"))


def even_odds_sums(numbers):
    even_index_sum = sum(numbers[::2])
    odd_index_sum = sum(numbers[1::2])

    return [even_index_sum, odd_index_sum]


print(even_odds_sums([10, 20, 30, 40, 50, 60]))


def plus_minus(numbers):
    if not numbers:
        0

    result = numbers[0]

    result += sum(numbers[1::2])

    result -= sum(numbers[2::2])

    return result


print(plus_minus([10, 20, 30, 40, 50, 60]))
