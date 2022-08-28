def narcissistic(value):
    valueCheck = 0
    powerCheck = 1

    while valueCheck < value:
        valueCheck = 0
        for digit in str(value):
            digit = int(digit) ** powerCheck
            valueCheck += digit

        if valueCheck == value:
            return True
        powerCheck += 1

    return False


print(narcissistic(7))
