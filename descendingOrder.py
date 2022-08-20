def descending_order(num):
    # Bust a move right here
    num = list(str(num))
    num.sort(reverse=True)
    return "".join(int(num))


print(descending_order(42145))
