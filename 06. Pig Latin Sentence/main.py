def pl_sentence(sentence):
    vowels = {"a", "e", "i", "o", "u"}
    output = []
    s = sentence.split()

    for word in s:
        unique_vowels = vowels & set(word.lower())
        if len(unique_vowels) >= 2:
            result = word + "way"
            output.append(result)
        elif word[0].lower() in vowels:
            result = word + "yay"
            output.append(result)
        else:
            result = word[1:] + word[0] + "ay"
            output.append(result)

    result = " ".join(output)

    return result


print(pl_sentence("this is a test translation"))
