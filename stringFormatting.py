def print_formatted(number):
    width = len(str(bin(number))) - 2
    for i in range(1, number + 1):
        d = str(i)
        o = str(oct(i))
        h = str(hex(i).upper())
        b = str(bin(i))
        print(
            d.rjust(width), o[2:].rjust(width), h[2:].rjust(width), b[2:].rjust(width)
        )


n = int(input())
print_formatted(n)
