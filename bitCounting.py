def count_bits(n):
    binary = str(bin(n)[2:])
    bits = 0
    for num in binary:
        if num == "1":
            bits += 1

    return bits


print(count_bits(7))
