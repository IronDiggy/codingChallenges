def get_count(sentence):
    count = 0
    for letter in sentence:
        if letter in ["a", "e", "i", "o", "u"]:
            count += 1
    return count


print(get_count("abcdefghijklmnopqrstuvwxyz"))
