import textwrap


def wrap(string, max_width):
    stringInput = ""
    stringList = []
    letterCount = 0
    for letter in string:
        stringInput += letter
        letterCount += 1
        if len(stringInput) == max_width:
            stringList.append(stringInput)
            stringInput = ""
        elif letterCount == len(string):
            stringList.append(stringInput)

    wordWrap = "\n".join(stringList)
    return wordWrap


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
