def swap_case(s):
    word = ""

    for letter in s:
        try:
            if letter.isupper() == True:
                letter = letter.lower()
                word = word + letter
            elif letter.islower() == True:
                letter = letter.upper()
                word = word + letter
            elif letter.islower() == False and letter.isupper() == False:
                word = word + letter
        except:
            continue

    return word


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
