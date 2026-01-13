import string


def pig_latin(word):
    vowels = {"a", "e", "i", "o", "u"}
    unique_vowels = vowels & set(word.lower())
    punctuation = ""

    if word[-1] in string.punctuation:
        punctuation = word[-1]
        word = word[:-1]

    if len(unique_vowels) >= 2:
        result = word + "way"
    elif word[0].lower() in vowels:
        result = word + "yay"
    else:
        result = word[1:] + word[0] + "ay"

    return result + punctuation


print(pig_latin("wine."))
print(pig_latin("apple."))
print(pig_latin("banana."))
