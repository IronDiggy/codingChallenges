def spin_words(sentence):
    sentence = sentence.split()
    refactoredSentence = []

    for word in sentence:
        if len(word) >= 5:
            word = word[::-1]
            refactoredSentence.append(word)
        else:
            refactoredSentence.append(word)

    return " ".join(refactoredSentence)


print(spin_words("Hey fellow warriors"))
