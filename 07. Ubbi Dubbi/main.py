def ubbi_dubbi(word):
    vowels = {"a", "e", "i", "o", "u"}
    output = []

    for letter in word.lower():
        if letter in vowels:
            output.append("ub" + letter)
        else:
            output.append(letter)

    result = "".join(output)

    if word[0].isupper():
        return result.capitalize()
    else:
        return result


print(ubbi_dubbi("Elephant"))
print(ubbi_dubbi("Octopus"))
